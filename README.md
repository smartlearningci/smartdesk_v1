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

## Preparar e executar (Ubuntu/Linux, Python 3.11+)

```bash
git clone https://github.com/smartlearningci/smartdesk.git
cd smartdesk
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
