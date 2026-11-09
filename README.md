# SmartDesk — Sistema de Gestão de Pedidos de Suporte

Projeto pedagógico da NexaServ (60 colaboradores, equipa de TI com três técnicos e uma responsável). O MVP transforma a [especificação aprovada](docs/produto/03_mvp_backlog_e_aceitacao.md) numa aplicação local com **Python, FastAPI, HTML e SQLite**.

## Funcionalidades e regras

- Ana (colaboradora) cria e consulta os próprios tickets; pode comunicar que um ticket Resolvido continua com problema.
- Miguel (técnico) consulta tickets atribuídos, inicia tratamento e regista soluções.
- Sofia (responsável de TI) consulta todos, atribui e reatribui técnicos e fecha tickets Resolvidos após verificar a resolução, sem confirmação formal obrigatória de Ana.
- Estados: **Aberto → Em tratamento → Resolvido → Fechado**. Um ticket Resolvido pode regressar a Em tratamento; Fechado não pode ser reaberto.
- Categorias: **Equipamento, Software, Acessos**. Campos obrigatórios: título, descrição e categoria.

## Estrutura

| Caminho | Responsabilidade |
|---|---|
| `src/main.py` | Rotas HTTP, formulários e apresentação de erros |
| `src/services.py` | Regras de estados, validações e permissões |
| `src/auth.py` | Autenticação e perfis |
| `src/database.py` | Ligação e esquema SQLite |
| `src/templates/` | Interface HTML |
| `src/static/style.css` | Estilos |
| `scripts/create_demo_users.py` | Contas fictícias locais |
| `tests/` | Testes automatizados |
| `docs/` e `features/` | Especificação e Gherkin aprovados |

## Execução com Docker Compose (ensaio de formação)

Esta é a forma recomendada de executar o **smartdesk_v1** na sessão. Requer Git e Docker com Docker Compose. **Não é necessário instalar Python ou pacotes localmente.** Há apenas um serviço web `app`; os dados SQLite ficam num volume gerido por Docker.

### 1. Obter o projeto

```bash
git clone https://github.com/smartlearningci/smartdesk_v1.git
cd smartdesk_v1
```

### 2. Definir a chave de sessão local

O segredo **não está no código, no GitHub ou na imagem**. No terminal Bash (Linux/macOS), gerar uma chave aleatória usando Python dentro de um contentor e criar o ficheiro ignorado `.env`:

```bash
printf 'SMARTDESK_SESSION_SECRET=%s\n' "$(docker run --rm python:3.12-slim python -c 'import secrets; print(secrets.token_urlsafe(48))')" > .env
```

Não partilhar o ficheiro `.env` nem usar um segredo fixo. O Compose exige a variável `SMARTDESK_SESSION_SECRET` antes de iniciar o serviço.

### 3. Construir a imagem e criar contas locais

```bash
docker compose build
docker compose run --rm app python -m scripts.create_demo_users
```

O script pede interativamente as palavras-passe das três contas de ensaio. A base de dados é criada no volume `smartdesk_data` e permanece nas execuções seguintes. Utilizadores: `ana@nexaserv.test`, `miguel@nexaserv.test` e `sofia@nexaserv.test`. Não existem palavras-passe publicadas.

### 4. Arrancar e consultar

```bash
docker compose up -d
docker compose ps
docker compose logs -f app
```

Abrir **http://localhost:8080/login** (ou `http://127.0.0.1:8080/login`). O Compose publica **apenas** `127.0.0.1:8080` no computador, encaminhando para a porta 8000 do contentor.

O endpoint técnico `GET /health` devolve `{"status":"ok"}` quando a aplicação responde. Não verifica a base de dados e não substitui os testes de desempenho T-11/RNF-002.

Para sair da apresentação contínua dos logs, usar `Ctrl+C` (não pára o serviço).

### 5. Executar os testes e guardar os relatórios no computador

O serviço `tests` usa a mesma imagem Python, mas executa os testes com uma base SQLite temporária. **Não altera os utilizadores nem os tickets da demonstração.** Os relatórios são guardados numa pasta partilhada entre o contentor e o computador.

```bash
# Criar a pasta partilhada no computador
mkdir -p reports

# Construir a imagem de testes e executar os conjuntos
# (não é necessário instalar Python no computador)
docker compose build tests
docker compose run --rm tests
```

Abrir `reports/relatorio_global.html` no navegador. Existem ainda `unitarios.html`, `http.html`, `bdd.html`, os correspondentes ficheiros JUnit XML e `relatorio_global.json`. Verde = aprovado; vermelho = falha/erro; amarelo = ignorado; cinzento = não executado.

Em Linux, se o teu utilizador não tiver UID/GID 1000, executar assim para garantir permissões de escrita na pasta partilhada:

```bash
LOCAL_UID="$(id -u)" LOCAL_GID="$(id -g)" docker compose run --rm tests
```

**Limitação:** o conjunto BDD só verifica a presença dos identificadores US-001 a US-012, não executa os passos Gherkin. T-11 (desempenho) e T-12 (Chrome/Edge) continuam não executados. A matriz T-01 a T-20 não é marcada como aprovada apenas por existirem casos pytest aprovados. Ver [documentação detalhada da validação](docs/qualidade/03_validacao_automatizada.md).

### 6. Parar e recomeçar

```bash
# Testes de autenticação, permissões, negócio, API e health; sem instalação local
docker compose run --rm tests

# Parar e remover o contentor e a rede, preservando o volume SQLite
docker compose down

# Recomeçar, conservando os tickets e utilizadores
docker compose up -d
```

**Atenção:** `docker compose down -v` também elimina o volume e **todos os dados SQLite de ensaio**. Só usar se pretender reiniciar a demonstração do zero.

### Ficheiros de infraestrutura

| Ficheiro | Função |
|---|---|
| `Dockerfile` | Define imagem Python 3.12-slim, bibliotecas, utilizador sem privilégios e arranque `uvicorn src.main:app` |
| `compose.yaml` | Orquestra a aplicação web e um serviço opcional de testes, com pasta `./reports` partilhada |
| `.dockerignore` | Exclui `.env`, bases locais, caches e ambientes do contexto da imagem |
| `.gitignore` | Impede o versionamento de segredos, bases e ambientes locais |
| `requirements.txt` | Declara as bibliotecas Python, incluindo Jinja2 para templates HTML |
| `scripts/run_tests.py` | Executa os conjuntos pytest e gera JUnit XML, HTML e resumo global |
| `reports/` | Resultados gerados no computador; ignorados pelo Git e pela imagem |

**Limites:** ambiente local de formação; não publicar portas na rede nem expor à Internet. Os formulários continuam sem proteção CSRF e o cookie de sessão não exige HTTPS. O teste de `/health` está em `tests/test_health.py` e complementa, sem substituir, os testes RF/RNF já existentes.

## Execução sem Docker (alternativa histórica: Ubuntu/Linux, Python 3.11+)

```bash
git clone https://github.com/smartlearningci/smartdesk_v1.git
cd smartdesk_v1
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
export SMARTDESK_SESSION_SECRET="$(python -c 'import secrets; print(secrets.token_urlsafe(48))')"
python -m scripts.create_demo_users
uvicorn src.main:app --reload
```

Abrir **http://127.0.0.1:8000/login**. Contas fictícias: `ana@nexaserv.test`, `miguel@nexaserv.test`, `sofia@nexaserv.test`. O script solicita as palavras-passe; não existem palavras-passe de demonstração publicadas. A base de dados `smartdesk.sqlite3` é local e ignorada pelo Git.

## Testes

```bash
pytest -v
```

Os testes têm objetivos e referências RF/US/T nos respetivos ficheiros. Cobrem regras de negócio, autenticação, permissões e percursos HTTP. **Não existe evidência de execução dos testes nesta publicação.** O teste `test_bdd.py` verifica os identificadores dos 12 cenários, mas **não executa os passos BDD**. Permanecem por validar a execução BDD completa, o tempo de resposta (T-11/RNF-002) e os navegadores Chrome/Edge (T-12/RNF-004). A documentação aprovada continua em [docs/](docs/) e [features/tickets.feature](features/tickets.feature).

## Limitações e próximos passos

Esta aplicação destina-se a uma demonstração **local**, não a produção. Os formulários não dispõem ainda de proteção CSRF e o cookie de sessão não está configurado para HTTPS obrigatório; **não expor à Internet**. As condições de medição de desempenho serão definidas antes do T-11.

Depois da validação integral, a formação prosseguirá para Docker, Compose, CI/CD e cloud, sem acrescentar funcionalidades de negócio ao MVP.
