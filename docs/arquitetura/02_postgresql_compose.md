# SmartDesk V2 — PostgreSQL local com Docker Compose

## Objetivo e âmbito

Substituir a persistência operacional SQLite por PostgreSQL sem alterar
HTML, rotas HTTP, regras, requisitos RF-001..RF-009 ou US-001..US-012.
Preservar a documentação da V1. Não há serviços cloud nem ferramentas pagas.

## Arquitetura

- `app`: FastAPI, porta publicada apenas em `127.0.0.1:8080`.
- `db`: PostgreSQL 17, hostname `db` na rede default do Compose.
  A porta 5432 não é publicada no anfitrião.
- `postgres_data`: volume nomeado persistente da base.
- `tests`: usa `smartdesk_test` separada da BD de demonstração e
  partilha `./reports` com o computador.

`app` e `tests` aguardam `db` saudável com `pg_isready`.
O `DATABASE_URL` é construído pelo Compose a partir de `POSTGRES_DB`,
`POSTGRES_USER` e `POSTGRES_PASSWORD` do `.env`.
Não publicar `.env` no GitHub.

## Esquema e inicialização

`src/database.py` mantém as tabelas `users` e `tickets` e as
restrições de categorias, estados, perfis e chaves estrangeiras.
A função `initialize(db)` usa `CREATE TABLE IF NOT EXISTS`.
É executada no `lifespan` da aplicação e no script de utilizadores.

O script `docker/01_create_test_db.sh` cria `smartdesk_test` somente
na primeira inicialização de um volume PostgreSQL novo. Se o volume
já existir sem esta base, será necessário criá-la manualmente antes
de executar os testes. Os testes PostgreSQL apagam dados **apenas**
da base `smartdesk_test`, nunca da base de demonstração.

## Comandos

```bash
cp .env.example .env
# Substituir os valores de POSTGRES_PASSWORD e SMARTDESK_SESSION_SECRET.
mkdir -p reports
docker compose build
docker compose up -d db
docker compose run --rm -it app python -m scripts.create_demo_users
docker compose up -d app
docker compose run --rm tests
```

Abrir `http://localhost:8080/login` e `reports/relatorio_global.html`.
Para parar preservando os dados: `docker compose down`.
Para recomeçar: `docker compose up -d`.

## Estratégia de validação

Os testes existentes mantêm bases SQLite temporárias, permitindo verificar
a regressão das regras e dos endpoints. `tests/test_postgres.py`
verifica criação, leitura, atualização e persistência entre ligações,
além de login e criação HTTP em PostgreSQL.

A persistência após reinício real dos contentores é um ensaio manual:
criar ticket, anotar ID, executar `docker compose restart app db`,
voltar a consultar o mesmo ticket e registar o resultado.
Não declarar o ensaio aprovado sem evidência.

A verificação `test_bdd.py` apenas confirma identificadores; não executa
passos Gherkin. T-11 (desempenho) e T-12 (Chrome/Edge) permanecem pendentes.

## Limites

A V2 começa com uma base PostgreSQL nova e contas fictícias criadas de
novo. Não existe migração automática de dados SQLite anteriores.
O volume SQLite histórico não é apagado. Não expor a aplicação à Internet:
CSRF e HTTPS/cookies seguros continuam fora do MVP local.
