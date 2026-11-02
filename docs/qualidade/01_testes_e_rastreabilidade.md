# 6. Testes e Rastreabilidade do SmartDesk

## 6.1. Objetivo

Definir os testes previstos para o MVP e garantir a rastreabilidade entre requisitos, User Stories e cenários Gherkin.

Os cenários de referência encontram-se em `features/tickets.feature`.

## 6.2. Estratégia de testes

Serão utilizados quatro tipos de testes:

| Tipo | Objetivo |
|---|---|
| Unitários | Verificar regras de negócio isoladas |
| Integração | Verificar a interação entre backend e base de dados |
| Funcionais | Validar as funcionalidades e cenários Gherkin |
| Interface | Verificar o funcionamento no Chrome e Edge e a facilidade de utilização |

Os testes serão preparados e executados durante a implementação. Nesta fase, estão apenas especificados.

## 6.3. Testes previstos

| ID | Teste | Cenários Gherkin | Tipo principal |
|---|---|---|---|
| T-01 | Iniciar sessão com credenciais válidas | US-011, RT-006 | Funcional |
| T-02 | Rejeitar credenciais inválidas e terminar sessão | RT-019, RT-020 | Funcional |
| T-03 | Verificar permissões dos perfis | RT-003, RT-005, RT-016 | Funcional |
| T-04 | Criar ticket válido | US-001 | Funcional |
| T-05 | Validar categorias e campos obrigatórios | RT-007, RT-008, RT-017 | Unitário / Funcional |
| T-06 | Consultar os próprios tickets | US-002 | Funcional |
| T-07 | Consultar e filtrar todos os tickets | US-003, RT-011 | Funcional |
| T-08 | Atribuir ticket | US-004 | Funcional |
| T-09 | Consultar tickets atribuídos | US-005 | Funcional |
| T-10 | Iniciar tratamento | US-006 | Funcional |
| T-11 | Registar resolução e exigir solução | US-007, RT-009 | Unitário / Funcional |
| T-12 | Retomar tratamento | US-008 | Funcional |
| T-13 | Fechar ticket Resolvido | US-009 | Funcional |
| T-14 | Impedir transições inválidas | RT-001, RT-002, RT-004, RT-010, RT-018 | Unitário / Funcional |
| T-15 | Consultar histórico | US-010 | Integração |
| T-16 | Reatribuir técnico | US-012, RT-021 | Funcional |
| T-17 | Impedir reatribuição de ticket Fechado | RT-022 | Funcional |
| T-18 | Impedir operações do técnico anterior | RT-023 | Funcional |
| T-19 | Verificar persistência | RT-014 | Integração |
| T-20 | Verificar Chrome e Edge | RT-012 | Interface |
| T-21 | Verificar facilidade de utilização | RT-013 | Interface |
| T-22 | Verificar mensagens de erro | RT-015 | Funcional |

Nos testes de operações rejeitadas, será também verificado que os dados permanecem inalterados.

### Critério mensurável de RNF-002 — Teste T-21

O teste de facilidade de utilização será realizado com **5 participantes representativos do perfil Colaborador**, sem formação prévia nem ajuda durante a execução.

Cada participante deverá, numa única sessão de teste:

1. Iniciar sessão.
2. Criar um ticket com título, descrição e categoria.
3. Consultar o ticket criado e identificar corretamente o respetivo estado.

**Tempo máximo:** 5 minutos para completar as três tarefas, contado desde o início da primeira tarefa até à conclusão da terceira.

**Critério de aprovação:** pelo menos **4 dos 5 participantes (80%)** concluem corretamente todas as tarefas, dentro dos 5 minutos e sem intervenção do avaliador.

Para cada participante serão registados o tempo total, as tarefas concluídas, os erros e a eventual necessidade de ajuda. Qualquer participante que ultrapasse o tempo, precise de ajuda ou não conclua corretamente uma tarefa não conta como sucesso.

Este critério concretiza o RNF-002 sem introduzir novas funcionalidades.

## 6.4. Matriz de rastreabilidade das User Stories

| User Story | Requisitos | Testes |
|---|---|---|
| US-001 — Criar ticket | RF-002, RF-005, RF-006, RF-007 | T-04, T-05 |
| US-002 — Consultar próprios tickets | RF-002, RF-014 | T-03, T-06 |
| US-003 — Consultar todos os tickets | RF-004, RF-016 | T-07 |
| US-004 — Atribuir ticket | RF-004, RF-008 | T-08 |
| US-005 — Consultar atribuídos | RF-003 | T-09 |
| US-006 — Iniciar tratamento | RF-009 | T-03, T-10 |
| US-007 — Resolver ticket | RF-010 | T-11 |
| US-008 — Retomar tratamento | RF-011 | T-12 |
| US-009 — Fechar ticket | RF-012, RF-013 | T-03, T-13, T-14 |
| US-010 — Consultar histórico | RF-015 | T-15, T-19 |
| US-011 — Autenticação | RF-001, RNF-003 | T-01, T-02, T-03 |
| US-012 — Reatribuição | RF-004, RF-008, RF-015 | T-16, T-17, T-18 |

## 6.5. Rastreabilidade dos requisitos não funcionais

| Requisito | Testes |
|---|---|
| RNF-001 — Chrome e Edge | T-20 |
| RNF-002 — Interface simples | T-21 |
| RNF-003 — Autenticação e permissões | T-01, T-02, T-03, T-18 |
| RNF-004 — Persistência | T-15, T-19 |
| RNF-005 — Mensagens de erro | T-02, T-05, T-14, T-17, T-22 |

## 6.6. Critérios de conclusão

A validação do MVP exigirá:

1. Execução com sucesso dos 12 cenários principais.
2. Verificação das regras adicionais RT-001 a RT-023.
3. Confirmação das permissões dos três perfis.
4. Verificação das transições de estado e da reatribuição.
5. Confirmação da persistência dos tickets, soluções e históricos.
6. Funcionamento no Google Chrome e Microsoft Edge.
7. Verificação das mensagens de erro e da facilidade de utilização.

O critério mensurável de facilidade de utilização (RNF-002) deverá ser concretizado antes da execução dos testes.

## 6.7. Estado da qualidade

Nesta fase:

- Os testes estão identificados e relacionados com os cenários Gherkin.
- As 12 User Stories têm testes associados.
- Os 16 requisitos funcionais e os 5 não funcionais estão contemplados.
- Nenhum teste foi ainda implementado ou executado.

A execução e os resultados serão registados nas etapas posteriores de desenvolvimento.
