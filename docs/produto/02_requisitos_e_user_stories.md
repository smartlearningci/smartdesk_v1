# Passo 4 — Requisitos, User Stories e critérios de aceitação

**Estado:** Versão 2 aprovada.

## 1. Requisitos funcionais (RF)

| ID | Requisito | Descrição |
|---|---|---|
| RF-001 | Autenticação | Acesso através de email e palavra-passe, com identificação do perfil. |
| RF-002 | Criação de tickets | Registar os campos obrigatórios título, descrição e categoria: Equipamento, Software ou Acessos. |
| RF-003 | Consulta de tickets | Colaborador consulta os seus tickets; técnico consulta os atribuídos; responsável consulta todos. |
| RF-004 | Atribuição e reatribuição | Sofia atribui ou reatribui tickets, incluindo os que estão Em tratamento. |
| RF-005 | Início do tratamento | Técnico responsável altera o estado de Aberto para Em tratamento. |
| RF-006 | Resolução | Técnico regista a solução e altera o estado para Resolvido. |
| RF-007 | Regresso ao tratamento | Colaborador comunica que o problema persiste; ticket passa de Resolvido para Em tratamento. |
| RF-008 | Fecho | Apenas Sofia pode fechar tickets Resolvidos após verificar e confirmar a resolução, sem confirmação formal obrigatória do colaborador. Tickets Fechados não podem ser reabertos. |
| RF-009 | Supervisão | Sofia consulta tickets, categorias, estados e técnicos responsáveis. |

## 2. Requisitos não funcionais (RNF)

| ID | Requisito | Critério de verificação |
|---|---|---|
| RNF-001 | Usabilidade | O colaborador consegue criar um ticket sem conhecimentos técnicos, com campos e mensagens compreensíveis. |
| RNF-002 | Desempenho | As páginas principais respondem em até 3 segundos, em condições normais de utilização. Meta provisória aprovada; as páginas e condições de medição serão documentadas antes da execução dos testes. |
| RNF-003 | Segurança | Acesso autenticado e operações limitadas às permissões de cada perfil. |
| RNF-004 | Compatibilidade | A aplicação funciona no Chrome e Edge, em computador. |

## 3. User Stories (US)

| ID | Persona | User Story | Requisitos |
|---|---|---|---|
| US-001 | Ana | Como Ana, quero iniciar sessão com email e palavra-passe, para aceder aos meus pedidos em segurança. | RF-001, RNF-003 |
| US-002 | Ana | Como Ana, quero criar um ticket, para comunicar um problema informático. | RF-002, RNF-001 |
| US-003 | Ana | Como Ana, quero consultar os meus tickets, para acompanhar a resolução. | RF-003 |
| US-004 | Sofia | Como Sofia, quero atribuir e reatribuir tickets, para distribuir o trabalho pelos técnicos. | RF-004, RNF-003 |
| US-005 | Miguel | Como Miguel, quero consultar os tickets atribuídos, para organizar o meu trabalho. | RF-003 |
| US-006 | Miguel | Como Miguel, quero iniciar o tratamento de um ticket, para indicar que estou a resolver o problema. | RF-005 |
| US-007 | Miguel | Como Miguel, quero registar a solução e marcar o ticket como Resolvido, para documentar a intervenção. | RF-006 |
| US-008 | Ana | Como Ana, quero comunicar que o problema persiste, para que o ticket regresse a Em tratamento. | RF-007 |
| US-009 | Sofia | Como Sofia, quero acompanhar os tickets e fechar os resolvidos, para supervisionar o suporte. | RF-008, RF-009 |
| US-010 | Ana | Como Ana, quero um formulário simples com indicação dos campos obrigatórios e mensagens de erro claras, para criar tickets corretamente. | RF-002, RNF-001 |
| US-011 | Miguel | Como Miguel, quero consultar rapidamente os tickets atribuídos, para organizar o meu trabalho sem esperas desnecessárias. | RF-003, RNF-002 |
| US-012 | Ana | Como Ana, quero utilizar o SmartDesk no Chrome e no Edge, para conseguir aceder e criar tickets no navegador disponível. | RF-001, RF-002, RNF-004 |

As histórias US-010, US-011 e US-012 reforçam, respetivamente, usabilidade, desempenho e compatibilidade. A autenticação foi incluída para distinguir os três perfis. A reatribuição e o regresso ao tratamento decorrem da jornada aprovada. Não são introduzidas funcionalidades fora do MVP.

## 4. Critérios de aceitação em Gherkin

Os cenários de aceitação aprovados estão no ficheiro [features/tickets.feature](../../features/tickets.feature). Cada cenário identifica a respetiva User Story.

## 5. Matriz de rastreabilidade

| Requisito | User Stories relacionadas | Verificação |
|---|---|---|
| RF-001 | US-001, US-012 | Autenticação e acesso |
| RF-002 | US-002, US-010, US-012 | Criação e validação |
| RF-003 | US-003, US-005, US-011 | Consulta de tickets |
| RF-004 | US-004 | Atribuição e reatribuição |
| RF-005 | US-006 | Início de tratamento |
| RF-006 | US-007 | Registo da resolução |
| RF-007 | US-008 | Regresso ao tratamento |
| RF-008 | US-009 | Fecho e bloqueios |
| RF-009 | US-009 | Supervisão |
| RNF-001 | US-002, US-010 | Formulário e mensagens |
| RNF-002 | US-011 | Tempo de resposta |
| RNF-003 | US-001, US-004, US-009 | Autenticação e permissões |
| RNF-004 | US-012 | Chrome e Edge |

**Cobertura de rastreabilidade:** 13/13 requisitos associados a pelo menos uma User Story; 12/12 User Stories associadas a requisitos e com pelo menos um cenário Gherkin. A rastreabilidade não demonstra, por si só, cobertura integral de testes.

O cenário US-011 requer medição de tempo em condições de utilização previamente definidas. O US-012 requer execução nos dois navegadores. Os restantes cenários incluem verificações funcionais e de permissões.

## 6. Decisões confirmadas

1. Autenticação por **email e palavra-passe**.
2. Ana pode comunicar que o problema persiste e devolver um ticket de **Resolvido** a **Em tratamento**.
3. Apenas Sofia pode fechar tickets **Resolvidos**, após verificar a resolução, sem confirmação formal obrigatória de Ana.
4. Meta provisória de resposta das páginas principais: **até 3 segundos**, com condições de medição a documentar antes dos testes.
5. **Título, descrição e categoria** são obrigatórios na criação de tickets.

**Âmbito preservado:** perfis colaborador, técnico de suporte e responsável de TI; categorias Equipamento, Software e Acessos; estados Aberto, Em tratamento, Resolvido e Fechado. Fora do MVP: aplicação móvel, SMS, resolução automática por IA, integração de email e SLA complexo.
