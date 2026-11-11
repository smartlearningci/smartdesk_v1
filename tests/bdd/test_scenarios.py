"""Execução BDD real dos cenários funcionais do ficheiro aprovado.

T-11 exige medição sob condições definidas; T-12 exige Chrome e Edge reais.
São explicitamente ignorados, nunca aprovados por simulação HTTP.
"""
import pytest
from pytest_bdd import scenario, given, when, then, parsers
from src.database import connect
from src import services
from tests.conftest import login, person, create_ticket

FEATURE = "../../features/tickets.feature"

@scenario(FEATURE, "US-001 - Autenticação")
def test_t01(): pass
@scenario(FEATURE, "US-002 - Criar ticket")
def test_t02(): pass
@scenario(FEATURE, "US-003 - Consultar tickets")
def test_t03(): pass
@scenario(FEATURE, "US-004 - Atribuir e reatribuir ticket")
def test_t04(): pass
@scenario(FEATURE, "US-005 - Consultar tickets atribuídos")
def test_t05(): pass
@scenario(FEATURE, "US-006 - Iniciar tratamento")
def test_t06(): pass
@scenario(FEATURE, "US-007 - Registar resolução")
def test_t07(): pass
@scenario(FEATURE, "US-008 - Regressar ao tratamento")
def test_t08(): pass
@scenario(FEATURE, "US-009 - Acompanhar e fechar ticket")
def test_t09(): pass
@scenario(FEATURE, "US-010 - Validar campos obrigatórios")
def test_t10(): pass

@pytest.mark.skip(reason="T-11: condições de medição de desempenho ainda não definidas; não simular aprovação")
@scenario(FEATURE, "US-011 - Verificar desempenho")
def test_t11(): pass

@pytest.mark.skip(reason="T-12: exige navegador Chrome/Edge real, indisponível no TestClient")
@scenario(FEATURE, "US-012 - Compatibilidade")
def test_t12(): pass

@pytest.fixture
def ctx(env):
    client, path = env
    return {"client": client, "path": path, "ticket": None, "response": None}

def actor(ctx, email):
    with connect(ctx["path"]) as db:
        return person(db, email)

def ticket(ctx, state="Aberto", assigned=False):
    with connect(ctx["path"]) as db:
        t = create_ticket(db)
        if assigned:
            t = services.assign(db, person(db, "sofia@test"), t["id"], person(db, "miguel@test")["id"])
        if state != "Aberto":
            services.start(db, person(db, "miguel@test"), t["id"])
        if state in ("Resolvido", "Fechado"):
            services.resolve(db, person(db, "miguel@test"), t["id"], "Solução aplicada")
        ctx["ticket"] = services.get(db, t["id"])

def update(ctx, operation, email, *args):
    with connect(ctx["path"]) as db:
        ctx["ticket"] = operation(db, person(db, email), ctx["ticket"]["id"], *args)

@given("que Ana possui uma conta válida")
def ana_account(ctx): assert actor(ctx, "ana@test")["role"] == "colaborador"
@when("introduz o email e a palavra-passe corretos")
def valid_login(ctx): ctx["response"] = login(ctx["client"], "ana@test")
@then("consegue iniciar sessão")
def logged(ctx): assert ctx["response"].status_code == 303
@then("é identificada como colaboradora")
def identified(ctx): assert actor(ctx, "ana@test")["role"] == "colaborador"

@given("que Ana iniciou sessão")
def ana_logged(ctx): login(ctx["client"], "ana@test")
@when("cria um ticket com título e descrição")
def create_form(ctx): ctx["data"] = {"title": "Impressora", "description": "Não imprime"}
@when(parsers.parse('seleciona a categoria "{category}"'))
def choose_category(ctx, category):
    ctx["data"]["category"] = category
    ctx["response"] = ctx["client"].post("/tickets/new", data=ctx["data"], follow_redirects=False)
@then("o ticket é registado")
def created(ctx):
    assert ctx["response"].status_code == 303
    with connect(ctx["path"]) as db:
        ctx["ticket"] = dict(db.execute("SELECT * FROM tickets ORDER BY id DESC LIMIT 1").fetchone())
@then(parsers.parse('fica no estado "{state}"'))
def initial_state(ctx, state): assert ctx["ticket"]["state"] == state

@given("existem tickets de vários colaboradores")
def several_owners(ctx):
    ticket(ctx)
    with connect(ctx["path"]) as db:
        services.create(db, person(db, "outro@test"), "Outro", "Outro problema", "Software")
@when("consulta os tickets")
def list_ana(ctx): ctx["response"] = ctx["client"].get("/tickets")
@then("visualiza apenas os seus pedidos")
def only_own(ctx):
    assert "Impressora" in ctx["response"].text
    assert "Outro problema" not in ctx["response"].text
@then("os respetivos estados")
def states_visible(ctx): assert "Aberto" in ctx["response"].text

@given("que Sofia iniciou sessão como responsável de TI")
def sofia_logged(ctx): login(ctx["client"], "sofia@test")
@given(parsers.parse('existe um ticket no estado "{state}"'))
def existing_state(ctx, state): ticket(ctx, state, assigned=(state != "Aberto"))
@when("atribui o ticket a Miguel")
def assign_miguel(ctx): update(ctx, services.assign, "sofia@test", actor(ctx, "miguel@test")["id"])
@then("Miguel fica identificado como responsável")
def miguel_assigned(ctx): assert ctx["ticket"]["technician_id"] == actor(ctx, "miguel@test")["id"]
@when("Sofia reatribui o ticket a outro técnico")
def reassign(ctx): update(ctx, services.assign, "sofia@test", actor(ctx, "tecnico2@test")["id"])
@then("o novo técnico fica identificado como responsável")
def new_tech(ctx): assert ctx["ticket"]["technician_id"] == actor(ctx, "tecnico2@test")["id"]
@then(parsers.parse('o estado do ticket mantém-se "{state}"'))
def state_unchanged(ctx, state): assert ctx["ticket"]["state"] == state

@given("que Miguel iniciou sessão como técnico")
def miguel_logged(ctx): login(ctx["client"], "miguel@test")
@given("existem tickets atribuídos a Miguel")
def tickets_assigned(ctx): ticket(ctx, assigned=True)
@when("consulta a lista de tickets")
def list_miguel(ctx): ctx["response"] = ctx["client"].get("/tickets")
@then("visualiza os tickets que lhe estão atribuídos")
def tech_listing(ctx): assert "Impressora" in ctx["response"].text

@given("que Miguel possui um ticket atribuído")
def miguel_ticket(ctx): ticket(ctx, assigned=True)
@given(parsers.parse('o ticket está no estado "{state}"'))
def check_state(ctx, state): assert ctx["ticket"]["state"] == state
@when("inicia o tratamento")
def start(ctx): update(ctx, services.start, "miguel@test")
@then(parsers.parse('o estado passa a "{state}"'))
def state_changes(ctx, state): assert ctx["ticket"]["state"] == state

@given("que Miguel está a tratar um ticket")
def treating(ctx): ticket(ctx, "Em tratamento", assigned=True)
@when("regista a solução aplicada")
def solution(ctx): ctx["solution"] = "Substituído toner"
@when("assinala o ticket como resolvido")
def resolve(ctx): update(ctx, services.resolve, "miguel@test", ctx["solution"])
@then("a solução fica registada")
def solution_saved(ctx): assert ctx["ticket"]["resolution"] == ctx["solution"]

@given(parsers.parse('que Ana possui um ticket no estado "{state}"'))
def ana_ticket(ctx, state): ticket(ctx, state, assigned=True)
@given("o ticket está atribuído a Miguel")
def verify_assignment(ctx): miguel_assigned(ctx)
@when("comunica que o problema persiste")
def reopen(ctx): update(ctx, services.reopen, "ana@test")
@then(parsers.parse('o estado regressa a "{state}"'))
def returned(ctx, state): assert ctx["ticket"]["state"] == state
@then("Miguel mantém-se como responsável")
def same_tech(ctx): miguel_assigned(ctx)

@when("consulta a solução registada")
def consult_solution(ctx): assert ctx["ticket"]["resolution"] == "Solução aplicada"
@when("confirma a resolução sem exigir confirmação formal de Ana")
def confirm(ctx): ctx["confirmed"] = True
@when("fecha o ticket")
def close(ctx): update(ctx, services.close, "sofia@test", ctx["confirmed"])

@when("tenta criar um ticket sem um dos campos obrigatórios título, descrição ou categoria")
def invalid_forms(ctx):
    ctx["errors"] = []
    for field in ("title", "description", "category"):
        data = {"title": "Pedido", "description": "Problema", "category": "Equipamento"}
        data[field] = ""
        response = ctx["client"].post("/tickets/new", data=data)
        ctx["errors"].append((field, response))
@then("o ticket não é criado")
def no_creation(ctx):
    with connect(ctx["path"]) as db:
        assert db.execute("SELECT count(*) FROM tickets").fetchone()[0] == 0
@then("o campo em falta é identificado")
def missing_field(ctx):
    assert all(name == "category" and "categoria" in response.text.lower()
               or name == "title" and "título" in response.text.lower()
               or name == "description" and "descrição" in response.text.lower()
               for name, response in ctx["errors"])
@then("é apresentada uma mensagem clara")
def clear_message(ctx): assert all(response.status_code == 200 and 'role="alert"' in response.text for _, response in ctx["errors"])
