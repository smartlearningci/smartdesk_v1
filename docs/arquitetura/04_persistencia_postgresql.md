# SmartDesk V2 — PostgreSQL local

A aplicação mantém os mesmos endpoints, templates, regras de negócio e esquema lógico (`users` e `tickets`). A base operacional passa a PostgreSQL no serviço `db` do Compose. O SQLite permanece apenas para fixtures legadas com caminho explícito.

## Configuração

Copiar `.env.example` para `.env` e editar `POSTGRES_DB`, `POSTGRES_USER`, `POSTGRES_PASSWORD` e `SMARTDESK_SESSION_SECRET`. O Compose fornece `DATABASE_URL` ao serviço `web` usando o hostname interno `db`. Não publicar o `.env`.

## Inicialização e persistência

`src/database.py:initialize()` executa `CREATE TABLE IF NOT EXISTS` no arranque e na criação dos utilizadores de demonstração. Preserva as restrições e referências de `users` e `tickets`. O volume nomeado `postgres_data` mantém os dados após `docker compose down` e `up -d`. Nunca usar `down -v` para uma base que se pretende preservar.

O serviço `web` espera pelo healthcheck `pg_isready` do serviço `db`. A base não publica a porta 5432 no anfitrião. O Compose utiliza a sua rede interna padrão.

## Limites e testes

Não existe importação automática do volume SQLite antigo. Os testes existentes com ficheiros SQLite temporários continuam a validar regressão funcional. `tests/test_postgres.py` verifica PostgreSQL com esquemas temporários isolados. O ensaio de persistência após recriação de contentores deve ser executado manualmente, criando e consultando um ticket antes/depois de `docker compose down && docker compose up -d`. Só registar como aprovado quando houver evidência. T-11 e T-12 permanecem pendentes de medições e navegadores reais.
