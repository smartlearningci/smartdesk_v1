# SmartDesk — Sistema de Gestão de Pedidos de Suporte

Projeto prático de desenvolvimento de software, utilizado ao longo de uma formação sobre requisitos, GitHub, programação, testes, automação, containers e cloud.

## 1. Contexto do projeto

A **NexaServ** é uma empresa fictícia de consultoria e serviços tecnológicos, com 60 colaboradores e uma equipa de TI composta por três técnicos de suporte e uma responsável.

Atualmente, os pedidos de suporte informático são comunicados por email, telefone e mensagens, sendo acompanhados através de uma caixa de correio partilhada e de uma folha de cálculo.

Esta forma de trabalho provoca dificuldades:

- Pedidos que se perdem ou ficam sem resposta.
- Falta de clareza sobre o técnico responsável.
- Dificuldade em acompanhar o estado dos pedidos.
- Ausência de uma visão centralizada do trabalho da equipa de TI.

## 2. A solução SmartDesk

O **SmartDesk** será uma aplicação web interna para centralizar a gestão dos pedidos de suporte informático.

Permitirá acompanhar um pedido desde a sua criação até ao encerramento, identificando os responsáveis e registando o histórico das alterações.

O projeto será desenvolvido progressivamente, a partir de uma especificação aprovada.

## 3. Utilizadores do sistema

O SmartDesk terá três perfis:

| Perfil | Responsabilidades |
|---|---|
| Colaborador — Ana Martins | Criar tickets e acompanhar os seus pedidos |
| Técnico de suporte — Miguel Costa | Consultar tickets atribuídos, tratar e resolver problemas |
| Responsável de TI — Sofia Almeida | Consultar todos os tickets, atribuir e reatribuir técnicos, acompanhar e fechar pedidos |

Todos os utilizadores terão autenticação por email e palavra-passe próprios do SmartDesk.

## 4. Funcionalidades do MVP

A primeira versão incluirá:

- Autenticação e controlo de permissões.
- Criação e consulta de tickets.
- Categorias: Equipamento, Software e Acessos.
- Atribuição e reatribuição de técnicos.
- Tratamento e resolução de pedidos.
- Retoma do tratamento de tickets Resolvidos.
- Encerramento de tickets pela Responsável de TI.
- Consulta de estados, resoluções e histórico.
- Persistência de dados.
- Funcionamento no Google Chrome e Microsoft Edge.

### Estados de um ticket

**Aberto → Em tratamento → Resolvido → Fechado**

Um ticket Resolvido pode regressar a Em tratamento. Um ticket Fechado não pode ser reaberto.

A reatribuição do técnico é permitida antes do fecho e não altera o estado do ticket.

### Fora do MVP

Aplicação móvel, notificações SMS, integração com email, resolução automática com IA, gestão complexa de SLA, autenticação multifator e integração com serviços externos de identidade.

## 5. Arquitetura inicial

O SmartDesk terá três componentes principais:

```text
Utilizador (Chrome / Edge)
           |
        Frontend
           |
       API HTTPS
           |
        Backend
           |
      Base de dados
```

- **Frontend:** apresenta a interface web.
- **Backend:** executa as regras de negócio, autenticação e permissões.
- **Base de dados:** guarda utilizadores, tickets, soluções e histórico.

A escolha das tecnologias concretas será realizada antes da implementação.

## 6. Documentação do projeto

A documentação foi produzida progressivamente, desde o problema de negócio até à arquitetura e aos testes.

| Etapa | Documento | Conteúdo |
|---|---|---|
| 1 | [Problema e objetivos](docs/negocio/01_problema_e_objetivos.md) | Contexto, problema e objetivos |
| 2 | [Stakeholders e personas](docs/negocio/02_stakeholders_e_personas.md) | Utilizadores e necessidades |
| 3 | [Jornada e processo](docs/produto/01_jornada_e_processo.md) | Ciclo de vida de um ticket |
| 4 | [Requisitos e User Stories](docs/produto/02_requisitos_e_user_stories.md) | Requisitos funcionais e não funcionais |
| 5 | [MVP e backlog](docs/produto/03_mvp_backlog_e_aceitacao.md) | Funcionalidades prioritárias e aceitação |
| 6 | [Arquitetura inicial](docs/arquitetura/01_arquitetura_inicial.md) | Componentes e responsabilidades |
| 6 | [Testes e rastreabilidade](docs/qualidade/01_testes_e_rastreabilidade.md) | Plano de testes e ligação aos requisitos |

Os cenários de aceitação estão disponíveis em [features/tickets.feature](features/tickets.feature), escritos em Gherkin.

## 7. Estrutura do repositório

```text
smartdesk_v1/
├── README.md
├── docs/
│   ├── negocio/
│   │   ├── 01_problema_e_objetivos.md
│   │   └── 02_stakeholders_e_personas.md
│   ├── produto/
│   │   ├── 01_jornada_e_processo.md
│   │   ├── 02_requisitos_e_user_stories.md
│   │   └── 03_mvp_backlog_e_aceitacao.md
│   ├── arquitetura/
│   │   └── 01_arquitetura_inicial.md
│   └── qualidade/
│       └── 01_testes_e_rastreabilidade.md
├── features/
│   └── tickets.feature
├── src/                   # Código a desenvolver
└── tests/                 # Testes a implementar
```

As pastas `src/` e `tests/` representam a organização prevista para as próximas etapas. Não significam que já exista uma implementação.

## 8. Qualidade e rastreabilidade

A especificação inicial contém:

- 16 requisitos funcionais.
- 5 requisitos não funcionais.
- 12 User Stories.
- 35 cenários ou esquemas Gherkin.
- 22 grupos de testes previstos.

Cada User Story está relacionada com requisitos e testes.

**Estado atual:** os testes estão especificados, mas ainda não foram implementados nem executados.

## 9. Próximos passos da formação

O projeto será utilizado para acompanhar o ciclo de desenvolvimento de uma aplicação realista.

### Fase 1 — Especificação

**Concluída.**

Problema de negócio, personas, processo, requisitos, User Stories, MVP, arquitetura inicial e testes previstos.

### Fase 2 — Preparação do desenvolvimento

- Rever e consolidar a especificação.
- Selecionar as tecnologias de frontend, backend e base de dados.
- Organizar a estrutura do código.
- Preparar o ambiente de desenvolvimento.

### Fase 3 — Implementação

- Desenvolver progressivamente o MVP.
- Implementar autenticação e permissões.
- Implementar a gestão de tickets.
- Integrar frontend, backend e base de dados.

### Fase 4 — Testes e qualidade

- Implementar testes unitários, de integração e funcionais.
- Validar os cenários Gherkin.
- Corrigir problemas encontrados.
- Verificar a rastreabilidade entre requisitos, código e testes.

### Fase 5 — Containers e automação

- Preparar a execução dos componentes com Docker.
- Automatizar tarefas de construção e testes.
- Introduzir práticas de integração e entrega contínuas (CI/CD).

### Fase 6 — Evolução para cloud

- Preparar a aplicação para execução num ambiente cloud.
- Explorar conceitos de disponibilização, configuração e monitorização.
- Comparar a execução local com a execução em cloud.

Estas fases representam o percurso previsto da formação, não funcionalidades adicionais do MVP.

## 10. Estado do projeto

**Especificação inicial concluída e aprovada.**

A implementação da aplicação ainda não foi iniciada.

O repositório será atualizado progressivamente à medida que as etapas de desenvolvimento forem aprovadas e concluídas.
