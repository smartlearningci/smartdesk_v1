# 5. MVP, Backlog e Critérios de Aceitação do SmartDesk

## 5.1. Objetivo

Definir uma primeira versão pequena e demonstrável do SmartDesk, baseada nos requisitos e User Stories aprovados. O MVP acompanha um pedido desde a autenticação até ao fecho, incluindo a possibilidade de reatribuição.

## 5.2. Definição do MVP

Aplicação web interna para Google Chrome e Microsoft Edge, com três perfis: Colaborador (Ana Martins), Técnico de suporte (Miguel Costa) e Responsável de TI (Sofia Almeida).

O MVP permite autenticar e terminar sessão; aplicar permissões; criar e consultar tickets; atribuir e reatribuir técnicos; iniciar, resolver e retomar tratamento; fechar tickets Resolvidos; consultar estados, resoluções e históricos; e preservar dados entre sessões.

## 5.3. Backlog priorizado

P0: essencial para a primeira demonstração. P1: necessário para completar o MVP. P2: fora do MVP. P0 e P1 entram ambos no MVP.

| Ordem | ID | Funcionalidade | Prioridade | Entrega |
|---|---|---|---|---|
| 1 | US-011 | Autenticação e fim de sessão | P0 | MVP |
| 2 | US-001 | Criar ticket | P0 | MVP |
| 3 | US-003 | Consultar todos os tickets | P0 | MVP |
| 4 | US-004 | Atribuir ticket | P0 | MVP |
| 5 | US-005 | Consultar tickets atribuídos | P0 | MVP |
| 6 | US-006 | Iniciar tratamento | P0 | MVP |
| 7 | US-007 | Registar resolução | P0 | MVP |
| 8 | US-009 | Fechar ticket | P0 | MVP |
| 9 | US-002 | Consultar os próprios tickets | P1 | MVP |
| 10 | US-008 | Retomar tratamento | P1 | MVP |
| 11 | US-010 | Consultar histórico | P1 | MVP |
| 12 | US-012 | Reatribuir técnico | P1 | MVP |

## 5.4. O que entra no MVP

| Funcionalidade | Requisitos associados |
|---|---|
| Autenticação por email e palavra-passe | RF-001, RNF-003 |
| Permissões por perfil | RF-001 a RF-004, RNF-003 |
| Criação de tickets | RF-002, RF-005 a RF-007 |
| Consulta de tickets | RF-002 a RF-004, RF-014, RF-016 |
| Atribuição e reatribuição | RF-004, RF-008, RF-015 |
| Tratamento e resolução | RF-009 a RF-011 |
| Fecho de tickets | RF-012, RF-013 |
| Histórico | RF-015 |
| Persistência | RNF-004 |
| Mensagens de erro | RNF-005 |
| Compatibilidade Chrome e Edge | RNF-001 |
| Clareza da interface | RNF-002 |

## 5.5. O que fica para depois

Não fazem parte da primeira versão: aplicação móvel, notificações SMS, integração com email, resolução automática com IA, gestão complexa de SLA, recuperação automática de palavra-passe, autenticação multifator e integração com serviços externos de identidade.

## 5.6. Cenários principais de aceitação

Um cenário principal por User Story. A versão Gherkin integral encontra-se em `features/tickets.feature`.

| User Story | Dado | Quando | Então |
|---|---|---|---|
| US-001 | Ana autenticada como Colaborador | Cria ticket com campos obrigatórios | Ticket criado com identificador e estado Aberto |
| US-002 | Ana tem tickets registados | Consulta os seus pedidos | Visualiza apenas os seus tickets, estados e resoluções |
| US-003 | Sofia autenticada como Responsável de TI | Consulta tickets | Visualiza todos e pode consultar por técnico e estado |
| US-004 | Ticket Aberto | Sofia atribui a Miguel | Miguel fica responsável e o estado permanece Aberto |
| US-005 | Miguel tem tickets atribuídos | Consulta a sua lista | Visualiza tickets atualmente atribuídos |
| US-006 | Miguel tem ticket Aberto atribuído | Inicia tratamento | Estado Em tratamento, alteração registada |
| US-007 | Miguel tem ticket Em tratamento atribuído | Regista solução | Estado Resolvido, solução guardada |
| US-008 | Miguel tem ticket Resolvido atribuído | Retoma tratamento | Estado Em tratamento, alteração registada |
| US-009 | Sofia consulta ticket Resolvido | Fecha ticket | Estado Fechado |
| US-010 | Sofia consulta ticket com histórico | Abre histórico | Visualiza alterações, datas e utilizadores |
| US-011 | Ana tem conta ativa | Introduz credenciais válidas | Acede às funcionalidades de Colaborador |
| US-012 | Ticket não fechado atribuído a Miguel | Sofia reatribui | Novo técnico responsável, estado mantido e alteração registada |

## 5.7. Regras obrigatórias de aceitação

| Regra | Requisitos | Cenários |
|---|---|---|
| Credenciais inválidas impedem acesso | RF-001, RNF-003 | RT-019 |
| Fim de sessão impede operações autenticadas | RF-001 | RT-020 |
| Perfis e permissões | RF-001 a RF-004, RNF-003 | RT-003, RT-005, RT-006, RT-016 |
| Categorias e campos obrigatórios | RF-005, RF-006 | RT-007, RT-008, RT-017 |
| Transições permitidas e proibidas | RF-009 a RF-013 | RT-001 a RT-004, RT-009, RT-010, RT-018 |
| Reatribuição em estados permitidos | RF-008 | RT-021, RT-022 |
| Técnico anterior perde permissões | RF-003, RF-008 | RT-023 |
| Histórico e persistência | RF-015, RNF-004 | RT-014 |
| Consulta por técnico e estado | RF-016 | RT-011 |
| Chrome e Edge | RNF-001 | RT-012 |
| Interface clara | RNF-002 | RT-013 |
| Mensagens de erro | RNF-005 | RT-008, RT-015, RT-017, RT-019 |

## 5.8. Matriz de rastreabilidade do MVP

| Requisito | User Stories | Prioridade | MVP |
|---|---|---|---|
| RF-001 | US-011 | P0 | Sim |
| RF-002 | US-001, US-002 | P0/P1 | Sim |
| RF-003 | US-005, US-006, US-007 | P0 | Sim |
| RF-004 | US-003, US-004, US-012 | P0/P1 | Sim |
| RF-005 | US-001 | P0 | Sim |
| RF-006 | US-001 | P0 | Sim |
| RF-007 | US-001 | P0 | Sim |
| RF-008 | US-004, US-012 | P0/P1 | Sim |
| RF-009 | US-006 | P0 | Sim |
| RF-010 | US-007 | P0 | Sim |
| RF-011 | US-008 | P1 | Sim |
| RF-012 | US-009 | P0 | Sim |
| RF-013 | US-009 e regras transversais | P0 | Sim |
| RF-014 | US-002 | P1 | Sim |
| RF-015 | US-010, US-012 | P1 | Sim |
| RF-016 | US-003 | P0 | Sim |
| RNF-001 | Transversal | P0 | Sim |
| RNF-002 | Transversal | P1 | Sim |
| RNF-003 | US-011 e transversal | P0 | Sim |
| RNF-004 | Transversal | P0 | Sim |
| RNF-005 | Transversal | P0 | Sim |

## 5.9. Condições para considerar o MVP concluído

1. Os três perfis conseguem autenticar-se e terminar sessão.
2. As permissões são respeitadas.
3. É possível criar, atribuir, tratar, resolver e fechar um ticket.
4. É possível retomar um ticket Resolvido.
5. É possível reatribuir um ticket não fechado.
6. A reatribuição não altera o estado e retira ao técnico anterior as permissões de tratamento.
7. O histórico regista alterações de estado e de técnico.
8. Os dados persistem após nova sessão.
9. Os 12 cenários principais e as regras obrigatórias são validados.
10. A aplicação funciona no Google Chrome e Microsoft Edge.

## 5.10. Justificação das escolhas

A autenticação identifica o utilizador e permite aplicar permissões. O ciclo de criação, atribuição, tratamento, resolução e fecho é o percurso mínimo demonstrável. A reatribuição demonstra a redistribuição do trabalho. A consulta e o histórico permitem acompanhar os pedidos e responsabilidades. As funcionalidades P1 completam o âmbito aprovado após a primeira demonstração. Não são introduzidas novas personas, categorias ou estados.
