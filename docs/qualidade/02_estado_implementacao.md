# Estado da implementação e evidências de teste

**Âmbito:** MVP SmartDesk aprovado, sem alteração de requisitos, User Stories ou Gherkin.

## Implementação

- Interface HTML: `src/templates/` e `src/static/style.css`.
- HTTP e formulários: `src/main.py`.
- Regras de negócio: `src/services.py`.
- Autenticação e sessões: `src/auth.py`.
- Persistência SQLite: `src/database.py`.
- Testes: `tests/test_auth.py`, `test_permissions.py`, `test_ticket_rules.py`, `test_api.py` e `test_bdd.py`.

## Registo de execução

| Categoria | Estado | Evidência |
|---|---|---|
| Testes unitários de regras e permissões | Criados; execução por verificar | `tests/test_ticket_rules.py`, `tests/test_permissions.py` |
| Testes HTTP e autenticação | Criados; execução por verificar | `tests/test_api.py`, `tests/test_auth.py` |
| BDD — 12 cenários aprovados | Passos ainda não automatizados | `features/tickets.feature` |
| T-11 — tempo de resposta | Não executado | Requer condições de medição |
| T-12 — Chrome e Edge | Não executado | Requer ensaio em ambos os navegadores |

**Teste criado** significa código de verificação existente; **teste executado** exige registo de execução; **teste aprovado** exige resultado obtido conforme ao esperado. A existência de um ficheiro ou de uma asserção não comprova aprovação.

## Comando de execução

```bash
pytest -v
```

Registar data, ambiente, total de testes recolhidos, aprovados, falhados, ignorados e não executados após cada execução. Não interpretar a presença dos identificadores US no ficheiro BDD como execução dos cenários.

## Limitações

Falta executar e avaliar a suíte, automatizar os passos BDD em português, medir RNF-002 e verificar Chrome/Edge. A aplicação não está preparada para exposição pública (proteção CSRF e HTTPS/cookies seguros pendentes).
