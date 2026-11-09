# Passo 5 — MVP, backlog e critérios de aceitação

**Estado:** Proposta aprovada.

## 1. MVP proposto

O MVP SmartDesk permite demonstrar um percurso completo de suporte informático:

1. **Ana** inicia sessão e cria um ticket de impressora na categoria **Equipamento** — estado **Aberto**.
2. **Sofia** consulta o pedido e atribui-o a **Miguel** — estado **Aberto**.
3. **Miguel** consulta o ticket e inicia o tratamento — estado **Em tratamento**.
4. **Miguel** regista a solução — estado **Resolvido**.
5. **Sofia** verifica e confirma a resolução e fecha o ticket, sem confirmação formal obrigatória de Ana — estado **Fechado**.

**Percurso alternativo:** se Ana comunicar que o problema persiste, um ticket **Resolvido** regressa a **Em tratamento**, mantendo o técnico responsável, salvo reatribuição por Sofia.

O percurso é pequeno e demonstrável, mas cobre o ciclo de vida essencial do SmartDesk.

## 2. Backlog por prioridade

- **P0 — Essencial:** necessário para demonstrar o percurso completo.
- **P1 — Complementar:** necessário para cumprir o MVP aprovado, embora não seja indispensável à primeira demonstração.
- **P2 — Posterior:** melhorias para depois da primeira versão demonstrável.

| Prioridade | US | Funcionalidade | Decisão |
|---|---|---|---|
| P0 | US-001 | Autenticação por email e palavra-passe, com três perfis | MVP |
| P0 | US-002 | Criar ticket com título, descrição e categoria | MVP |
| P0 | US-003 | Ana consultar os seus tickets | MVP |
| P0 | US-004 | Sofia atribuir tickets aos técnicos | MVP |
| P0 | US-005 | Miguel consultar os tickets atribuídos | MVP |
| P0 | US-006 | Miguel iniciar tratamento | MVP |
| P0 | US-007 | Miguel registar resolução | MVP |
| P0 | US-009 | Sofia acompanhar e fechar tickets | MVP |
| P1 | US-008 | Ana comunicar problema persistente e devolver ticket a Em tratamento | MVP |
| P1 | US-010 | Validação de campos obrigatórios e mensagens claras | MVP |
| P1 | US-011 | Consulta de tickets com resposta até 3 segundos | MVP |
| P1 | US-012 | Funcionamento no Chrome e Edge | MVP |

**Nota:** A reatribuição de tickets prevista na US-004 faz parte do MVP, mesmo não sendo necessária ao percurso principal. P0 e P1 indicam a ordem de trabalho, não exclusões do MVP nem prioridades dos tickets. Não existe campo de prioridade por ticket no MVP.

## 3. Incluído no MVP e evolução posterior

**Incluído:** autenticação; criação e consulta de tickets; atribuição e reatribuição; tratamento e resolução; regresso ao tratamento; supervisão e fecho; validações dos campos obrigatórios (título, descrição e categoria); permissões; compatibilidade Chrome/Edge; meta provisória de resposta até 3 segundos.

**Fora do MVP:** aplicação móvel, notificações SMS, integração automática com email, resolução automática por IA e gestão avançada de SLA. Estas funcionalidades não serão especificadas nem implementadas nesta fase.

**Perfis:** colaborador (Ana Martins), técnico de suporte (Miguel Costa), responsável de TI (Sofia Almeida).

**Categorias:** Equipamento, Software e Acessos.

**Estados:** Aberto, Em tratamento, Resolvido e Fechado.

## 4. Critérios de aceitação em Gherkin

O ficheiro [`features/tickets.feature`](../../features/tickets.feature) contém os **12 cenários principais**, um por User Story (US-001 a US-012), revistos para o MVP. A simplificação substitui os 16 cenários anteriores, mantendo os identificadores.

A reatribuição, o fecho exclusivo por Sofia e a proibição de reabrir tickets fechados continuam a ser regras obrigatórias, mesmo sem cenários negativos independentes nesta versão simplificada.

## 5. Regras de negócio obrigatórias

| Regra | Comportamento esperado |
|---|---|
| Perfis | Colaborador, técnico e responsável de TI têm permissões distintas. |
| Categorias | Apenas Equipamento, Software e Acessos. |
| Estados | Aberto, Em tratamento, Resolvido e Fechado. |
| Reatribuição | Sofia pode reatribuir tickets, incluindo os que estão Em tratamento. |
| Regresso ao tratamento | Ana pode devolver um ticket Resolvido a Em tratamento. |
| Fecho | Apenas Sofia pode fechar um ticket Resolvido, após verificar a resolução, sem confirmação formal obrigatória de Ana. |
| Ticket fechado | Não pode ser reaberto. |

Estas regras devem continuar a ser verificadas na fase de testes.

## 6. Critério de conclusão do MVP

O MVP estará demonstrável quando:

- Ana conseguir iniciar sessão, criar um ticket e acompanhar o seu estado.
- Sofia conseguir atribuir e reatribuir tickets.
- Miguel conseguir consultar, tratar e resolver os tickets atribuídos.
- Ana conseguir comunicar que uma resolução não funcionou.
- Sofia conseguir supervisionar e fechar um ticket resolvido.
- As permissões, categorias, estados e regras de transição forem respeitados.
- Os critérios de usabilidade, desempenho e compatibilidade forem verificados.

**Nota:** O objetivo de até 3 segundos é provisório e requer medição em condições previamente definidas. A compatibilidade exige verificação no Chrome e no Edge.

## 7. Rastreabilidade

O MVP mantém as 12 User Stories e os requisitos RF-001 a RF-009 e RNF-001 a RNF-004 aprovados no [Passo 4](02_requisitos_e_user_stories.md). Cada cenário em `features/tickets.feature` identifica a sua User Story. Não foram acrescentadas novas personas nem funcionalidades.
