    Controle de Treinamento de Jedi's

Sistema desenvolvido para controle de treinamentos da Ordem Jedi, com monitoramento de habilidades, validade e alertas de instabilidade na Força.

O objetivo deste sistema é permitir o cadastro de personagens, gerenciar missões e acompanhar o controle de perda de habilidades. Além disso, o sistema contará com uma tela inicial em formato de dashboard para facilitar a visualização e o planejamento.

Os aplicativos que compõem o sistema são:

    -Cadastro
    -Alertas
    -Treinamrntos
    -Dashboard

-------------------------------------------------------------

    *CADASTRO*

Nesta área haverá a opção de cadastrar novos personagens.

Os campos disponíveis para cadastro são:

    Holofoto 3x4
    Código Jedi
    Nome completo
    Templo/Base
    Turno
    Rank:
       - Padawan
       - Cavaleiro Jedi
       - Mestre Jedi

----------------------------------------------------------------

    *Missões (Treinamentos)*

Cada Jedi poderá possuir missões associadas, que representam seus treinamentos.

Campos:

    Nome da missão
    Data de início
    Data de validade
    Status:
    Conectado à Força (ativo)
    Desconectado da Força (vencido)
    Relatórios

------------------------------------------------------------------

    *Treinamentos Jedi*

Cadastro dos treinamentos disponíveis no sistema.

Campos:

    Nome do treinamento
    Carga horária
    Tempo de validade
    Conhecimentos obrigatórios
    Alertas 

O sistema realizará o monitoramento da validade das habilidades.

Alertas serão gerados nos seguintes períodos:

90 dias antes
60 dias antes
30 dias antes
10 dias antes

---------------------------------------------------------

    *Dashboard*

Tela inicial com visão geral do sistema.

Indicadores:

    Habilidades vencidas
    Habilidades próximas do vencimento
    Habilidades válidas

-------------------------------------------------------------------

    *Área Administrativa*

Gestão completa do sistema.

Permite:

    Gerenciamento de Jedi
    Gerenciamento de treinamentos
    Controle de permissões de acesso
    Anexos

------------------------------------------------------

    *Tecnologias Utilizadas*
-Python
-Django
-SQLite ou PostgreSQL
-HTML / CSS
-Bootstrap

----------------------------------------------------------

    *Como rodar o projeto*
    
python manage.py runserver