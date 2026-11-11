# Plano de validação do MVP SmartDesk

**Estado:** implementação de testes e geração de relatórios; resultados por verificar. Preservam-se os requisitos e o ficheiro Gherkin aprovados.

## Convenções

- **Criado:** existe código de teste.
- **Executado:** existe um caso no JUnit XML de uma execução.
- **Aprovado:** o caso executado terminou sem falha, erro ou skip.
- **Falhado:** uma asserção não correspondeu ao esperado.
- **Erro:** falha técnica ou de preparação.
- **Ignorado:** o executor marcou skip (amarelo).
- **Não executado:** não há resultado ou falta ambiente/execução (cinzento).

O relatório global apresenta totais de **casos de teste** por conjunto e, em separado, o estado dos **20 IDs T**. Um teste pode cobrir mais de um ID; não se somam ambos os números.

## Matriz de aceitação — condições, ação e resultado esperado

| ID | RF/RNF | US | Condição inicial | Ação | Resultado esperado |
|---|---|---|---|---|---|
| T-01 | RF-001 RNF-003 | US-001 | Ana tem conta válida | Login correto | Sessão iniciada |
| T-02 | RF-002 RNF-001 | US-002 | Ana autenticada | Criar ticket Equipamento | Ticket Aberto |
| T-03 | RF-003 | US-003 | Tickets de várias pessoas | Ana consulta lista | Só os seus tickets |
| T-04 | RF-004 RNF-003 | US-004 | Ticket Aberto | Sofia atribui e reatribui | Técnico atualizado, estado mantido |
| T-05 | RF-003 | US-005 | Miguel tem tickets atribuídos | Consultar lista | Só os atribuídos |
| T-06 | RF-005 | US-006 | Ticket Aberto atribuído | Miguel inicia | Em tratamento |
| T-07 | RF-006 | US-007 | Ticket Em tratamento | Miguel regista solução | Resolvido, solução persistida |
| T-08 | RF-007 | US-008 | Ticket Resolvido de Ana | Ana comunica persistência | Em tratamento, mesmo técnico |
| T-09 | RF-008 RF-009 | US-009 | Ticket Resolvido | Sofia verifica e fecha | Fechado |
| T-10 | RF-002 RNF-001 | US-010 | Ana autenticada | Omitir separadamente cada campo | Criação recusada, mensagem clara |
| T-11 | RF-003 RNF-002 | US-011 | Ambiente e medição documentados | Medir páginas principais | Cada resposta até 3 segundos |
| T-12 | RF-001 RF-002 RNF-004 | US-012 | Chrome e Edge reais | Login e criação em cada um | Ambos funcionam |
| T-13 | RF-001 RNF-003 | US-001 | Conta válida | Password errada | Login recusado |
| T-14 | RF-008 RNF-003 | US-009 | Ticket Resolvido | Miguel tenta fechar | Operação recusada |
| T-15 | RF-008 | US-009 | Ticket Fechado | Ana tenta reabrir | Operação recusada |
| T-16 | RF-004 | US-004 | Ticket Em tratamento | Sofia reatribui | Estado preservado |
| T-17 | RF-003 RF-005 RNF-003 | US-006 | Ticket atribuído a outro | Técnico tenta alterar | Operação recusada |
| T-18 | RF-009 | US-009 | Vários tickets | Sofia consulta | Vê todos, estados e responsáveis |
| T-19 | RF-002 | US-002 | Ana autenticada | Testar categorias válidas/inválidas | Só as três aprovadas |
| T-20 | RF-008 | US-009 | Ticket Resolvido | Fecho por Sofia após verificação | Fecha sem confirmação formal de Ana |

Não há IDs RT documentados nesta versão; não foram criados.

## Organização

- **Unitários:** `tests/test_ticket_rules.py`, `tests/test_permissions.py`, `tests/test_mvp.py`. Exercitam serviços e SQLite isolado.
- **Integração HTTP:** `tests/test_auth.py`, `tests/test_api.py`. Exercitam formulários, sessão, autorização e persistência.
- **BDD:** `tests/bdd/test_scenarios.py`. Executa com pytest-bdd os cenários funcionais aprovados em `features/tickets.feature`; T-11 e T-12 ficam explicitamente ignorados até haver medições/navegadores reais. `tests/test_bdd.py` é apenas uma verificação documental e não integra o conjunto BDD.

## Execução

Dentro da pasta do repositório, com Docker Compose e `.env` preparado:

```bash
docker compose build
docker compose run --rm --no-deps web python -m scripts.run_validation
```

São criados `reports/unit/junit.xml`, `reports/unit/index.html`, equivalentes em `integration/` e `bdd/`, e `reports/index.html` com o resumo global. O diretório `reports/` é montado no computador e ignorado pelo Git. A execução continua entre conjuntos mesmo após falhas e devolve código não zero quando algum conjunto falha.

**Limitações:** o teste de desempenho T-11 exige condições de medição previamente definidas; T-12 exige execução em Chrome e Edge. O estado destes testes não pode ser aprovado com TestClient. A execução de testes e Docker deverá ser comprovada por resultados reais, não pela publicação do código.

## Validação PostgreSQL V2

O conjunto `postgres` usa `tests/test_postgres.py` com esquemas temporários e verifica inicialização idempotente, criação, leitura por nova ligação, atribuição, tratamento, resolução, fecho e operação proibida. Relatórios previstos em `reports/postgres/`. A persistência após recriação dos contentores (`docker compose down` e `up -d`, sem `-v`) exige ensaio operacional separado e evidência real. Os testes SQLite originais continuam isolados. A publicação do código não comprova resultados.
