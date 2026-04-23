# Design System

## Visão Arquitetural

O GS Voucher adota arquitetura de monólito modular em Django, organizado em apps por domínio, com camada de Services obrigatória para regras de negócio. Views são finas (thin views, fat services). Comunicação entre domínios ocorre via Services ou Django Signals — nunca via import direto de models entre apps.

A aplicação é servida como único deploy em instância EC2 na AWS, com banco PostgreSQL em RDS e armazenamento de arquivos em S3. A interface é majoritariamente SSR (Django Templates), com endpoints REST (DRF) usados em situações específicas: scan de QR Code pelo agente, carregamento assíncrono em dashboards.

Há quatro perfis de usuário acessando a mesma aplicação, cada um com seu conjunto de rotas, templates e permissões: Administrador, Gerente de posto, Agente Golden Sat e Motorista. A separação é lógica (middleware + decorators), não física.

## Stack Técnica

| Camada        | Tecnologia                         |
|---------------|------------------------------------|
| Linguagem     | Python                             |
| Framework     | Django                             |
| API           | Django REST Framework              |
| Banco         | PostgreSQL                         |
| Frontend      | Django Templates                   |
| Storage       | AWS S3                             |
| E-mail        | SMTP                               |
| Testes        | pytest + pytest-django             |
| Qualidade     | ruff + mypy                        |
| Tarefas Agen. | django-contrab                     |
| QR Code       | qrcode (lib Python)                |
| Deploy        | Docker + EC2                       |


## Estrutura de Módulos

- `core/`           Models base, utilitários compartilhados, settings da aplicação
- `accounts/`       Autenticação e gestão de usuários (todos os perfis).
- `reports/`        Exportação de relatórios (Excel, CSV, PDF) e geração da fatura mensal.
- `routes/`         Cadastro de rotas de viagem e associação com postos
- `stations/`       Cadastro e gestão de postos homologados, atribuição de gerente e agente.
- `vouchers/`       Ciclo de vida do voucher: emissão, validação, consumo, cancelamento, expiração.

## Padrões Transversais

### BaseModel
Todo modelo de domínio herda de `core.BaseModel`, que fornece:
- `id`: UUIDField, primary_key
- `created_at`: DateTimeField (auto_now_add)
- `updated_at`: DateTimeField (auto_now)
- `is_active`: BooleanField (default=True)

### Deleção
Soft-delete via `is_active=False` é o padrão. Hard-delete apenas em tabelas de log técnico ou pivôs simples sem valor de auditoria. A camada de queryset custom (ActiveManager) garante que consultas padrão filtrem `is_active=True`, reduzindo o risco de expor dados inativos por engano.

### Service Layer
Toda regra de negócio vive em `<app>/services/.` Views e serializers orquestram, nunca implementam regra. Um service recebe dados já validados (pelo form/serializer), consulta/atualiza models, aplica regras, publica sinais. Serviços recebem dependências por parâmetro (repositórios, event_bus) sempre que isso facilitar testes.

### Comunicação entre Apps
Ordem de preferência para comunicação entre bounded contexts:
1.	Chamada direta a Service do outro app (import de serviço, não de model).
2.	Django Signals para efeitos colaterais desacoplados (ex: quando voucher transita para CONSUMED, signal dispara cálculo em reports).

Proibido: import direto de models entre apps. Se for necessário, crie uma função em services/ que exponha o que o app vizinho precisa.


## Decisões Arquiteturais (ADRs)

- **ADR-001** - Monólito modular
  - Decisão: monólito modular em vez de microserviços.
  - Racional: escala e orçamento não justificam complexidade operacional de serviços distribuídos; equipe pequena; monólito bem modularizado resolve 100% do problema.
  - Consequências: necessidade de disciplina interna para não quebrar limites de apps; mais fácil de deployar e operar.

- **ADR-002**: UUID como PK
  - Decisão: UUID em vez de autoincrement.
  - Racional: evita enumeração de recursos via URL, facilita merge de bases, permite geração client-side se necessário.
  - Consequências: índices maiores; performance levemente inferior em joins muito grandes (irrelevante neste volume).

- **ADR-003**: Soft-delete
  - Decisão: soft-delete via is_active=False como padrão.
  - Racional: auditoria financeira exige reversibilidade; dados nunca somem do histórico.
  - Consequências: queries padrão precisam filtrar; usar manager default que já faz isso

- **ADR-004**: DRF
  - Decisão: Django REST Framework para endpoints de API.
  - Racional: documentação OpenAPI automática superior; melhor ergonomia para consumo; padrão conhecido pela equipe.

- **ADR-005**: AWS S3 como storage
  - Decisão: S3 para storage de arquivos (relatórios, QR Codes renderizados, futuros anexos).
  - Racional: menor complexidade, menos superfície de ataque, SEO e acessibilidade facilitados, equipe produtiva na stack; SPA não traz valor claro para este caso.
  - Consequências: partes mais dinâmicas (scan do QR, atualização de fatura) ficam em endpoints REST pontuais consumidos via HTMX.

- **ADR-006**: SSR como padrão de UI
  - Decisão: Django Templates (SSR) com HTMX + Alpine.js para interações dinâmicas. Sem SPA.
  - Racional: menor complexidade, menos superfície de ataque, SEO e acessibilidade facilitados, equipe produtiva na stack; SPA não traz valor claro para este caso.
  - Consequências: partes mais dinâmicas (scan do QR, atualização de fatura) ficam em endpoints REST pontuais consumidos via HTMX.

- **ADR-007**: Autenticação não padrão para motorista
  - Decisão: motorista autentica com CPF + access_token gerado pelo admin. Não tem senha.
  - Racional: motoristas usam o sistema raramente, muitas vezes uma única vez. Gerenciar senhas teria altíssimo custo operacional (reset, esquecimento) e baixo ganho de segurança no contexto. Token single-use-ish (reemissível), entregue pelo admin, é suficiente.
  - Consequências: necessário cuidado extra com rate limiting e expiração; admin tem responsabilidade de comunicar token por canal seguro.

- **ADR-008**: QR Code assinado com HMAC
  - Decisão: QR Code contém payload JSON + assinatura HMAC-SHA256.
  - Racional: impede falsificação; permite validação offline do formato antes de consultar banco (mas banco é sempre a fonte da verdade do estado).

- **ADR-009:** Separação de perfis no mesmo app
  - Decisão: apps e deploy únicos; separação de perfis via URL namespace + permission mixin + template base por perfil.
  - Racional: quatro apps separados seriam over-engineering; a separação lógica é suficiente.
  - Consequências: disciplina para não misturar views de perfis diferentes no mesmo arquivo; manter convenção de pastas views/<perfil>_views.py.

- **ADR-010:** Fatura mensal automatizada, pagamento fora do sistema
  - Decisão: sistema gera PDF e Excel de fatura; pagamento é feito fora (transferência bancária, outro sistema).
  - Racional: integrar com sistema de pagamento é complexo e fora do escopo do MVP; gerar documento auditável resolve 90% do problema.

## Estratégia de Testes

### Pirâmide

- Unitários: pytest - Services, state machine, validações de regra
- Integração: pytest-django - Views, templates, serializers, queryset, filters
- E2E: pytest - Fluxo completo do voucher de emissão a fatura

### Principios

- Testes escritos antes da implementação (TDD) para regras de negócio.
- Services testados com factory-boy para criação de fixtures; sem mocks de model.
- Testes de contrato de view validam: template usado, contexto esperado, redirect em caso de perfil errado.
- Testes de API validam: status code, payload, permissões, isolamento entre postos.
- Teste específico de isolamento (RN-09): gerente do posto A nunca enxerga voucher do posto B, nem por ID direto.
- Teste de state machine cobre todas as transições válidas e bloqueia todas as inválidas.


## Observabilidade (a definir)

Observabilidade completa é pós-MVP (logging estruturado detalhado, métricas, tracing). No MVP, garantimos o mínimo para operar e depurar

Logs de aplicação
  - Python logging, saída para stdout (coletado pelo log driver do container). Nível INFO em prod, DEBUG em dev.

Auditoria de negócio:
  - VoucherAuditLog é append-only no próprio banco, consultável pelo admin via Django admin.

Erros não tratados:
  - Sentry (free tier) integrado em prod. Alerta por e-mail.

Health check:
  - /health/ retornando status do DB e app. Monitorado por ping externo a cada minuto.
  
Métricas de negócio:
  - Dashboard no Django admin com contadores por estado de voucher (suficiente para MVP).