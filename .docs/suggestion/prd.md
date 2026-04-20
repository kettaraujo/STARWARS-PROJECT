# PRD

## Sumário Executivo

O GS Voucher é um sistema de benefícios interno voltado para motoristas parceiros da operação Parada Segura do Grupo Golden Sat. Seu objetivo é incentivar que motoristas realizem paradas em postos homologados pela empresa, entregando um voucher digital de valor pré-definido que pode ser consumido dentro das dependências do posto.

A premissa central é o binômio segurança operacional e rastreabilidade financeira. Motoristas recebem incentivo concreto para parar em locais seguros; o Grupo Golden Sat e os postos parceiros obtêm histórico completo de emissões, validações e consumos; a conciliação mensal com cada posto é automática e auditável.

O sistema é uma aplicação web multi-perfil: Administradores (Golden Sat) emitem e controlam vouchers, Gerentes de posto registram consumos e geram relatórios, Agentes Golden Sat alocados em cada posto validam vouchers, e Motoristas acessam seus vouchers por CPF e token de uso único.

Público-alvo inicial: 7 postos homologados, cada um com 1 gerente e 1 agente dedicado. Número de motoristas é variável e alto — cada viagem tende a ser com motorista diferente. MVP previsto em 8 semanas de desenvolvimento.

## Problema e Oportunidade

### Contexto do Negócio

O roubo de cargas é um problema crônico no Brasil, com números crescentes a cada ano. Um dos pontos mais vulneráveis da cadeia de transporte são paradas de descanso e abastecimento: o motorista desce do veículo, a carga fica exposta, e quadrilhas especializadas atacam nesse intervalo.

Para enfrentar esse cenário, o Grupo Golden Sat mantém a operação Parada Segura, uma rede de postos homologados taticamente posicionados em rotas de risco. Um posto Parada Segura oferece vigilância reforçada, agente do Grupo Golden Sat em tempo integral, e protocolos de segurança pactuados — condições muito superiores às de um posto qualquer.

O desafio operacional é que a rede só cumpre seu papel se os motoristas efetivamente escolherem os postos homologados em vez de pararem em qualquer lugar da rota. Isso requer um mecanismo de incentivo.

### Problemas Específicos
- Motoristas não têm incentivo direto para parar em posto homologado em vez de outro mais próximo ou mais conveniente.
- O Grupo Golden Sat não tem visibilidade sobre quais motoristas efetivamente usaram a rede, nem sobre o padrão de uso por rota.
- A conciliação financeira entre Golden Sat e postos parceiros depende hoje de registros informais, sujeitos a erro e disputa.
- Não há rastreabilidade fim a fim: dado um gasto registrado por um posto, é difícil comprovar que motorista, em que rota, com qual voucher.

### Oportunidade

Um sistema de voucher digital resolve os quatro problemas acima simultaneamente: (a) cria incentivo concreto e imediato ao motorista (R$ 40 para gastar no posto), (b) entrega relatórios gerenciais para Golden Sat e postos, (c) formaliza o fluxo financeiro com histórico auditável, e (d) permite rastreio fim a fim de cada voucher emitido.

A solução deve ser leve e específica para o contexto: uma aplicação web acessível em desktop e mobile, sem exigência de download de app, pois muitos motoristas usam o sistema uma única vez em uma viagem específica.

## Objetivo

### Objetivos de Produto

1. Garantir que 100% dos motoristas elegíveis recebam e consigam consumir seu voucher sem atrito operacional.
2. Produzir histórico completo e auditável de todas as transações: emissão, atribuição, apresentação, validação e consumo.
3. Reduzir o ciclo de conciliação financeira Golden Sat ↔ posto parceiro de múltiplos dias para geração automática de fatura mensal.
4. Aumentar mensurável de paradas em postos homologados, mediante adoção do incentivo financeiro.
5. Entregar MVP funcional em até 4 semanas de desenvolvimento.

### Não-Objetivos

- Aplicativo mobile nativo (iOS/Android) ou PWA instalável. O motorista acessa via navegador comum.
- Acúmulo de vouchers — cada voucher é independente e tem validade de 48 horas.
- Multi-tenant (atender operações de múltiplas empresas no mesmo sistema).
- Integração com ERP contábil da Golden Sat (a fatura mensal é exportada em PDF/Excel; lançamento no ERP é manual no MVP).
- Integração com sistema de pagamento (não há pagamento direto dentro do sistema; a fatura é usada fora).
- Emissão automática de vouchers baseada em telemetria do veículo — no MVP, emissão é ação manual do administrador.
- Split de valor entre combustível, refeição e descanso — o voucher é uma única cota que o posto pode consumir livremente nas categorias acordadas.

## Personas

- Motoristas: Individuo que será beneficiado com o voucher para utilização dentro dos postos homologados.
- Gerentes dos Postos: Parceiro da Parada Segura, responsável pelo registro de gastos dentro dos postos.
- Agentes do Grupo Golden Sat: Funcionário do Grupo Golden Sat, responsável pela validação dos vouchers nos postos.
- Administradores de Conta: Responsável pela criação e gerenciamento de usuários, atribuição e controle de vouchers

## Histórias de Usuário

- Administrador:
    - Como administrador, quero criar um voucher atribuído a um motorista e uma rota específicos, para que o benefício seja liberado rapidamente sob demanda do embarcador. (RF-15, RF-16, RF-17)
    - Como administrador, quero cadastrar motoristas informando CPF e gerando automaticamente um token de acesso, para que o motorista possa fazer login sem precisar lembrar de senha. (RF-04)
    - Como administrador, quero cadastrar e editar postos homologados, atribuindo gerente e agente a cada um, para manter a rede sempre consistente. (RF-09, RF-10, RF-11)
    - Como administrador, quero criar e editar rotas, atribuindo os postos homologados disponíveis, para definir onde cada voucher pode ser consumido. (RF-12, RF-13, RF-14)
    - Como administrador, quero extrair relatórios consolidados cruzando vouchers, postos e rotas, para apoiar decisões operacionais e comerciais. (RF-06, RF-08)

- Gerente do Posto: 
    - Como gerente de posto, quero ver a lista de vouchers validados no meu posto em determinado período, para registrar os consumos à medida que acontecem. (RF-21)
    - Como gerente de posto, quero registrar o valor consumido em um voucher, para que o sistema reflita corretamente a transação. (RF-20)
    - Como gerente de posto, quero extrair meu relatório mensal em PDF ou Excel, para conferir e conciliar a fatura com o Grupo Golden Sat. (RF-06, RF-07, RF-08)
    - Como gerente de posto, quero ter garantia de que não consigo ver dados de outros postos, para respeitar a política de dados da operação. (RF-07)

- Agente Golden Sat:
    - Como agente, quero escanear o QR Code do motorista pelo celular e receber retorno imediato se o voucher é válido, para agilizar a entrada no posto. (RF-19)
    - Como agente, quero que um voucher não possa ser validado duas vezes, para evitar fraude por print de tela ou compartilhamento.


- Motorista: 
    - Como motorista, quero entrar no sistema com meu CPF e um token que recebi, para acessar meu voucher sem ter que criar conta ou memorizar senha. (RF-05)
    - Como motorista, quero ver o QR Code do meu voucher assim que entrar no sistema, para apresentá-lo ao chegar no posto. (RF-18)
    - Como motorista, quero saber em qual posto ou postos posso usar meu voucher, para escolher minha parada com confiança.
    - Como motorista, quero saber por quanto tempo meu voucher é válido, para não deixar vencer sem aproveitar.

## Regras de Negócio

Decisões normativas que regem o ciclo do voucher, separadas dos requisitos funcionais para dar peso e facilitar futuras revisões

- RN-01: Valor padrão do voucher é R$ 40,00, parametrizável em configurações do sistema - Permite ajuste sem redeploy conforme política comercial
- RN-02: Voucher expira em 48 horas após a emissão. Após expiração, torna-se inutilizável - Incentiva consumo imediato; evita estoque indefinido de obrigrações financeiras.
- RN-03: Voucher não é acumulativo. Motorista pode receber múltiplos vouchers, mas cada um é consumido parcialmente ou integralmente - Simplifica controle e conciliação.
- RN-04: Voucher só pode ser consumido em posto que pertence à rota atribuída - Garante aderência ao proósito de incentivar parada em rota de risco mapeada. 
- RN-05: Cada voucher é validado (scan) uma única vez. Segunda apresenta é rejeitada - Evita fraude por print ou foto do QR Code.
- RN-06: Valor consumido registrado pelo gerente não pode exceder o valor do voucher - Garante previsibilidade financeira para a Golden Sat
- RN-07: Valor consumido registrado pode ser menor que o valor do voucher (consumo parcial); o saldo não é reembolsado - Simplifica; alinhado à lógica de 'incentivo', não 'crédito'.
- RN-08: Motorista só pode ter um voucher em status OPEN por rota simultaneamente. - Evita acúmulo e uso duplicado na mesma rota.
- RN-09: Gerente só visualiza vouchers consumidos em seu prórpio posto - LGPD + política comercial (isolamento entre postos concorrentes).
- RN-10: Agente só visualiza/valida vouchers em seu próprio posto - Mesmo princípio de isolamento.
- RN-11: Fatura mensal é gerada por posto, consolidando todos os vouchers com consumo registrado no mês fechado - Modelo de conciliação definido com postos parceiros
- RN-12: Voucher pode ser cancelado pelo administrador antes da validação. Após validação, torna-se imutável. - Preserva integridade contábil.

## Ciclo de Vida do Voucher

O voucher é a entidade central do sistema. Seu ciclo de vida é formalizado nos seguintes estados:
- OPEN - Emitido e atribuído. QR Code válido. Aguardando apresentação no posto - Admin (ao criar)
- VALIDATED - Agente escaneou o QR Code no posto. Consumo autorizado - Agente (ao scan)
- CONSUMED - Gerente registrou valor consumido. Pronto para conciliação - Gerente (ao registrar)
- EXPIRED - Passou de 48h sem ser validado. Inutilizável. - Sistema (automático)
- CANCELED - Admin cancelou antes da validação. Inutilizável - Admin

## Requisitos Funcionais

### Autenticação
- RF-01: O sistema deve permitir login com usuário e senha para administradores, gerentes e agentes.
- RF-02: O sistema deve distinguir perfis de Admin, Gerente, Agente e Motorista, exibindo a interface correta para cada um.
- RF-03: O sistema deve permitir logout explícito pelo usuário.
- RF-04: O admin deve poder cadastrar motorista informando CPF, gerando automaticamente um token de acesso único.
- RF-05: O motorista deve poder fazer login com CPF + token gerado.

### Cadastros
- RF-09: O admin deve poder criar, editar e desativar postos homologados.
- RF-10: Todo posto deve ter um gerente atribuído no momento da criação.
- RF-11: Todo posto deve ter um agente atribuído no momento da criação.
- RF-12: O admin deve poder criar, editar e desativar rotas de viagem.
- RF-13: Toda rota deve ter pelo menos um posto atribuído.
- RF-14: O admin deve poder adicionar ou remover postos de uma rota existente.

### Vouchers
- RF-15: O admin deve poder criar um voucher com valor parametrizado (padrão R$ 40), gerando um QR Code único, com validade de 48 horas.
- RF-16: Todo voucher deve ser atribuído a exatamente um motorista no momento da criação.
- RF-17: Todo voucher deve ser atribuído a exatamente uma rota no momento da criação.
- RF-18: O voucher criado deve ficar disponível ao motorista em até 5 segundos após a criação.
- RF-19: O agente deve poder validar o voucher escaneando o QR Code pelo celular ou tablet.
- RF-20: O gerente do posto deve poder registrar o valor consumido (parcial ou total) de um voucher validado.
- RF-21: O gerente do posto deve poder listar e gerenciar os vouchers validados/consumidos em seu posto.
- RF-22: O admin deve poder cancelar um voucher em estado OPEN.

### Relatórios
- RF-06: Admins e gerentes devem poder extrair seus dados a qualquer momento.
- RF-07: O sistema deve garantir isolamento: um posto não pode ver dados de outro.
- RF-08: Exportação de relatórios deve suportar os formatos Excel, CSV e PDF.
- RF-23: O sistema deve gerar automaticamente a fatura mensal consolidada por posto no formato PDF, no primeiro dia útil de cada mês.

## Requisitos Não Funcionais

- Plataforma: Aplicação web responsiva. Suportar navegadores Chrome, Edge, Safari e Firefox nas duas últimas versões principais.
- Performance: Páginas devem carregar em < 2 segundos em conexão 4G típica. Geração de QR Code em < 1 segundo.
- Disponibilidade: Uptime alvo 99,5% em horário comercial estendido (6h às 22h). Janela de manutenção programada fora desse intervalo.
- Escalabilidade: Suportar pico de 500 vouchers ativos simultaneamente, até 100 scans/hora, sem degradação.
- Segurança: Autenticação por senha com hash PBKDF2. Token de motorista aleatório criptograficamente seguro com mínimo 8 caracteres alfanuméricos. QR Code contém payload assinado para impedir falsificação.
- LGPD: CPF do motorista é dado pessoal sensível. Armazenar com acesso restrito a admin. Log de acesso a dados de motorista. Direito de exclusão sob solicitação (anonimização após 5 anos da última atividade).
- Auditoria: Toda ação relevante (criação, validação, consumo, cancelamento de voucher) deve ser registrada em log imutável com timestamp, autor e dados anteriores/posteriores.
- Compatibilidade Mobile: Interface do motorista e do agente deve ser plenamente funcional em telas a partir de 360px.

## Jornada Principal do Voucher

1. Emissão: Administrador cria o voucher no sistema, selecionando motorista (existente ou novo), rota e, opcionalmente, valor customizado. Sistema gera QR Code e deixa o voucher em estado OPEN.
2. Acesso: Motorista recebe externamente seu CPF e token de acesso. Acessa a URL pública do GS Voucher e faz login. Visualiza o voucher disponível com QR Code e informações da rota.
3. Apresentação: Ao chegar em um posto homologado, o motorista apresenta o QR Code ao agente Golden Sat posto.
4. Validação: Agente escaneia o QR Code. Sistema verifica: voucher existe, está OPEN, pertence à rota do posto, dentro da validade. Se sim, transita para VALIDATED. Se não, retorna motivo específico (expirado, rota divergente, já validado).
5. Consumo: Motorista usa o benefício dentro do posto (refeição, descanso, pequenas compras conforme acordo comercial). Ao final, gerente do posto registra no sistema o valor efetivamente consumido (≤ valor do voucher). Voucher transita para CONSUMED.
6. Conciliação: No primeiro dia útil de cada mês, sistema gera fatura consolidade por posto com todos os vouchers em estado CONSUMED no mês anterior. Fatura exportada em PDF e Excel, disponível para gerente e admin. Pagamento efetivo do Golden Sat ao posto ocorre fora do sistema.

## Métricas de Sucesso

- 100% dos vouchers emitidos têm rastro auditável (quem criou, quem atribuiu, quem validou, onde foi consumido, quanto).
- Tempo médio de validação no posto < 1 minuto.
- Zero inconsistência entre valor consumido e valor conciliado para pagamento.
- Zero vazamento de dados entre usuários (verificado em teste).
- Aumento mensurável de paradas nos postos homologados