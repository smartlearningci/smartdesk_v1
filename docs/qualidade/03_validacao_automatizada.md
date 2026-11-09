# Validação automatizada do MVP — proposta implementada

## Identificação e limites
Referências oficiais: `docs/produto/02_requisitos_e_user_stories.md`,
`docs/qualidade/01_testes_e_rastreabilidade.md` e `features/tickets.feature`.
Não existem identificadores RT documentados. A matriz T-01..T-20 é uma matriz
de aceitação, **não** uma lista de 20 funções pytest independentes.

## Condições comuns
Os testes pytest usam uma base SQLite temporária, independente dos dados
da demonstração, e utilizadores fictícios criados pela fixture `env`.
Ação: executar a função de serviço ou a rota HTTP indicada.
Resultado esperado: os estados, permissões e mensagens indicados abaixo.

| ID | Objetivo / condições iniciais → ação → resultado esperado | Requisito | US | Teste existente |
|---|---|---|---|---|
| T-01 | Ana registada → login e logout → sessão iniciada e terminada | RF-001, RNF-003 | US-001 | test_auth.py |
| T-02 | Ana autenticada → cria ticket válido → estado Aberto | RF-002, RNF-001 | US-002 | test_ticket_rules.py, test_api.py |
| T-03 | Tickets de vários colaboradores → Ana consulta → só os seus | RF-003 | US-003 | test_permissions.py, test_api.py |
| T-04 | Ticket Aberto → Sofia atribui e reatribui → responsável atualizado | RF-004, RNF-003 | US-004 | test_permissions.py, test_api.py |
| T-05 | Miguel com/sem atribuições → consulta → apenas tickets atribuídos | RF-003 | US-005 | test_permissions.py (parcial) |
| T-06 | Ticket Aberto atribuído → Miguel inicia → Em tratamento | RF-005 | US-006 | test_ticket_rules.py, test_api.py |
| T-07 | Ticket Em tratamento → Miguel resolve → solução persistida e Resolvido | RF-006 | US-007 | test_ticket_rules.py, test_api.py |
| T-08 | Ticket Resolvido → Ana devolve → Em tratamento e mesmo técnico | RF-007 | US-008 | test_ticket_rules.py, test_api.py |
| T-09 | Ticket Resolvido → Sofia confirma fecho → Fechado | RF-008, RF-009 | US-009 | test_ticket_rules.py, test_api.py |
| T-10 | Falta título/descrição/categoria → criar → rejeição e erro claro | RF-002, RNF-001 | US-010 | test_ticket_rules.py (regras), test_api.py (título) |
| T-11 | Condições de medição documentadas → medir páginas → até 3 segundos | RF-003, RNF-002 | US-011 | NÃO EXECUTADO |
| T-12 | Chrome e Edge → Ana autentica/cria → funciona nos dois | RF-001, RF-002, RNF-004 | US-012 | NÃO EXECUTADO |
| T-13 | Palavra-passe incorreta → login → acesso recusado | RF-001, RNF-003 | US-001 | test_auth.py |
| T-14 | Miguel tenta fechar → operação recusada | RF-008, RNF-003 | US-009 | test_permissions.py |
| T-15 | Ticket Fechado → reabrir → operação recusada | RF-008 | US-009 | test_ticket_rules.py |
| T-16 | Ticket Em tratamento → Sofia reatribui → estado preservado | RF-004 | US-004 | test_permissions.py |
| T-17 | Ticket de outro técnico → alterar → HTTP 403 | RF-003, RF-005, RNF-003 | US-006 | test_permissions.py |
| T-18 | Tickets de vários utilizadores → Sofia consulta → visão global | RF-009 | US-009 | test_permissions.py (parcial) |
| T-19 | Três categorias válidas e outra inválida → criar → aceites/rejeitada | RF-002 | US-002 | test_ticket_rules.py |
| T-20 | Sofia sem/com confirmação → fechar → recusado/aceite | RF-008 | US-009 | test_ticket_rules.py |

## Organização real dos testes
- **Unitários/regras**: `test_ticket_rules.py`, `test_permissions.py`, `test_mvp.py`.
- **Integração HTTP**: `test_api.py`, `test_auth.py`, `test_health.py`.
- **Gherkin/rastreabilidade**: `test_bdd.py` apenas verifica identificadores US.
  Os passos dos cenários em `features/tickets.feature` **não estão automatizados**.
- **Saúde HTTP**: GET `/health` devolve `{"status":"ok"}`; verificação
  técnica sem T específico, não substitui desempenho T-11.

## Execução Docker
Na pasta do projeto:

```bash
cp .env.example .env
# Editar .env e atribuir SMARTDESK_SESSION_SECRET com pelo menos 32 caracteres.
mkdir -p reports
docker compose build tests
docker compose run --rm tests
```

O serviço `tests` não altera o volume SQLite `smartdesk_data`.
Em Linux, se a pasta `reports` não pertencer ao UID/GID 1000:
```bash
LOCAL_UID="$(id -u)" LOCAL_GID="$(id -g)" docker compose run --rm tests
```

Abrir `reports/relatorio_global.html` no navegador. Cada conjunto tem
`.xml` (JUnit) e `.html`; existe ainda `relatorio_global.json`.
Os ficheiros são regenerados a cada execução. Se pytest falhar, o comando
termina com código diferente de zero.

**Cores:** verde aprovado, vermelho falha/erro, amarelo ignorado,
cinzento não executado. Não se inventam resultados. A matriz T-01..T-20
permanece pendente de validação integral individual, mesmo que haja testes
pytest aprovados que cubram parcialmente os requisitos. T-11, T-12 e passos
BDD requerem execução específica.

**Estado de evidência:** o código e o comando foram publicados; não há
evidência de execução de Docker ou pytest nesta alteração.
