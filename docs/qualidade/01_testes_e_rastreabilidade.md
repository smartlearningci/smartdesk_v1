# Passo 6 — Testes previstos e rastreabilidade

**Estado:** Proposta aprovada. Os testes estão definidos, mas **não foram implementados nem executados**.

## 1. Estratégia de testes

1. **Testes de regras de negócio:** verificam validação de campos, permissões e mudanças de estado.
2. **Testes funcionais e de integração:** verificam operações do SmartDesk em conjunto e o registo correto dos dados.
3. **Testes de aceitação e qualidade:** verificam os percursos dos utilizadores, a compatibilidade dos navegadores e o tempo de resposta.

## 2. Testes principais — cenários Gherkin do MVP

Cada teste T-01 a T-12 corresponde a uma User Story e ao seu cenário principal em [features/tickets.feature](../../features/tickets.feature).

| Teste | Objetivo | User Story | Requisitos |
| --- | --- | --- | --- |
| T-01 | Confirmar que Ana inicia sessão com email e palavra-passe válidos. | US-001 | RF-001, RNF-003 |
| T-02 | Confirmar que Ana cria um ticket na categoria Equipamento, inicialmente Aberto. | US-002 | RF-002, RNF-001 |
| T-03 | Confirmar que Ana apenas consegue consultar os seus tickets. | US-003 | RF-003 |
| T-04 | Confirmar que Sofia atribui e reatribui tickets sem alterar indevidamente o estado. | US-004 | RF-004, RNF-003 |
| T-05 | Confirmar que Miguel consulta os tickets que lhe estão atribuídos. | US-005 | RF-003 |
| T-06 | Confirmar que Miguel inicia o tratamento de um ticket Aberto. | US-006 | RF-005 |
| T-07 | Confirmar que Miguel regista uma solução e altera o ticket para Resolvido. | US-007 | RF-006 |
| T-08 | Confirmar que Ana devolve um ticket Resolvido a Em tratamento, mantendo o técnico. | US-008 | RF-007 |
| T-09 | Confirmar que Sofia consulta a resolução e fecha o ticket. | US-009 | RF-008, RF-009 |
| T-10 | Confirmar separadamente que a ausência de título, descrição ou categoria impede a criação e apresenta mensagem clara. | US-010 | RF-002, RNF-001 |
| T-11 | Medir se as páginas principais de autenticação, criação e consulta de tickets respondem em até 3 segundos, sob condições de teste documentadas. | US-011 | RF-003, RNF-002 |
| T-12 | Confirmar que Ana inicia sessão e cria tickets no Chrome e no Edge. | US-012 | RF-001, RF-002, RNF-004 |

## 3. Testes adicionais — regras obrigatórias

Não acrescentam funcionalidades; verificam regras já aprovadas.

| Teste | Objetivo | User Story | Requisitos |
| --- | --- | --- | --- |
| T-13 | Rejeitar autenticação com palavra-passe incorreta. | US-001 | RF-001, RNF-003 |
| T-14 | Impedir que Miguel feche um ticket, mesmo que esteja Resolvido. | US-009 | RF-008, RNF-003 |
| T-15 | Impedir a reabertura de tickets Fechados. | US-009 | RF-008 |
| T-16 | Confirmar que Sofia pode reatribuir um ticket Em tratamento sem alterar o seu estado. | US-004 | RF-004 |
| T-17 | Confirmar que o técnico não pode alterar tickets atribuídos a outro técnico. | US-006 | RF-003, RF-005, RNF-003 |
| T-18 | Confirmar que Sofia consegue consultar todos os tickets, categorias, estados e técnicos responsáveis. | US-009 | RF-009 |
| T-19 | Confirmar que são aceites as três categorias aprovadas e rejeitadas categorias não previstas. | US-002 | RF-002 |
| T-20 | Confirmar que apenas Sofia fecha após verificar a resolução, sem exigir confirmação formal de Ana. | US-009 | RF-008 |

## 4. Matriz de rastreabilidade US ↔ RF/RNF ↔ testes

| User Story | Requisitos | Testes |
| --- | --- | --- |
| US-001 | RF-001, RNF-003 | T-01, T-13 |
| US-002 | RF-002, RNF-001 | T-02, T-19 |
| US-003 | RF-003 | T-03 |
| US-004 | RF-004, RNF-003 | T-04, T-16 |
| US-005 | RF-003 | T-05 |
| US-006 | RF-005 | T-06, T-17 |
| US-007 | RF-006 | T-07 |
| US-008 | RF-007 | T-08 |
| US-009 | RF-008, RF-009 | T-09, T-14, T-15, T-18, T-20 |
| US-010 | RF-002, RNF-001 | T-10 |
| US-011 | RF-003, RNF-002 | T-11 |
| US-012 | RF-001, RF-002, RNF-004 | T-12 |

**Cobertura de rastreabilidade prevista:** 12/12 User Stories e 13/13 requisitos (RF-001 a RF-009 e RNF-001 a RNF-004) têm testes relacionados. Isto não significa que os testes já passaram ou que a cobertura de execução esteja demonstrada.

## 5. Registo e apresentação dos resultados

Cada teste deverá identificar o **objetivo**, os **requisitos associados**, o **resultado esperado**, o **resultado obtido** e o **estado**:

| Estado | Significado |
|---|---|
| Passou | O comportamento observado corresponde ao esperado. |
| Falhou | O comportamento observado não corresponde ao esperado. |
| Não executado | O teste ainda não foi realizado. |

Posteriormente, poderá ser apresentado um relatório global com o total de testes executados, aprovados e falhados. Nesta etapa apenas se define o que será verificado.

**Observações:** T-11 requer medição das páginas principais em ambiente local de demonstração, com dados e condições documentados antes da execução; T-12 exige verificação em Chrome e Edge. Os cenários Gherkin mantêm os identificadores US-001 a US-012.

**Referências internas:** [Arquitetura inicial](../arquitetura/01_arquitetura_inicial.md), [Requisitos e User Stories](../produto/02_requisitos_e_user_stories.md), [MVP e backlog](../produto/03_mvp_backlog_e_aceitacao.md).
