# Estado da implementação e balanço da demonstração local

**Sessão:** demonstração local SmartDesk concluída segundo indicação do responsável pela formação. **Evidência disponível nesta atualização:** não foram comunicados logs, números de testes, relatórios JUnit/HTML ou falhas observadas. Não é possível confirmar aprovação de Docker, login, operações ou testes.

## Procedimento documentado (não constitui resultado de execução)

Na pasta do projeto, com Docker Compose:

```bash
cp .env.example .env
docker compose build
docker compose run --rm --no-deps -it web python -m scripts.create_demo_users
docker compose up -d
```

Aceder a `http://localhost:8080/login` com `ana@nexaserv.test`, `miguel@nexaserv.test` ou `sofia@nexaserv.test`, usando as palavras-passe escolhidas interativamente (mínimo oito caracteres). A chave de sessão fictícia de `.env` **não** é uma palavra-passe de login.

Executar a validação e consultar os resultados **se forem gerados**:

```bash
docker compose run --rm --no-deps web python -m scripts.run_validation
```

Relatório global previsto: `reports/index.html`; JUnit XML e HTML por conjunto em `reports/unit/`, `reports/integration/` e `reports/bdd/`. Para parar, sem eliminar o volume SQLite:

```bash
docker compose down
```

## O que está efetivamente confirmado

- **No repositório:** existem Dockerfile, Compose, script de contas fictícias, testes unitários, integração HTTP, cenários BDD, scripts de relatório e matriz T-01 a T-20.
- **Na execução local:** não foram fornecidos resultados verificáveis. **Aprovados: indeterminados; falhados: indeterminados; erros: indeterminados; ignorados: indeterminados; não executados: não quantificáveis com a evidência disponível.**
- **Falhas observadas:** não comunicadas; não interpretar como inexistentes.
- **Limitações conhecidas:** T-11 depende de medições em condições documentadas; T-12 exige ensaios reais em Chrome e Edge; proteção CSRF e HTTPS/cookies seguros não estão implementados para exposição pública.

## Próximos passos da formação

1. Recolher os resultados reais de `reports/` e registar os totais, sem converter testes ignorados ou não executados em aprovados.
2. Analisar e corrigir apenas falhas demonstradas pelos relatórios.
3. Prosseguir para CI/CD e cloud, preservando os requisitos e a arquitetura do MVP aprovado.

Referências: [plano de validação](03_plano_validacao.md), [rastreabilidade](01_testes_e_rastreabilidade.md) e [README](../../README.md).
