"""Testes de integração PostgreSQL: RF-001..RF-008; US-001..US-009.

Objetivo: criar, ler e atualizar tickets e confirmar persistência entre
ligações. Esperado: mesmos estados e permissões do MVP SQLite aprovado.
O reinício efetivo dos contentores é verificado manualmente.
"""
import os
import pytest
from src.database import connect, initialize
from src.auth import hash_password
from src import services


@pytest.fixture
def pg_users():
    # Proteção: nunca apagar dados da base de demonstração.
    if not os.getenv("DATABASE_URL", "").split("?")[0].endswith("/smartdesk_test"):
        pytest.fail("DATABASE_URL deve apontar exclusivamente para smartdesk_test")
    with connect() as db:
        initialize(db)
        db.execute("DELETE FROM tickets")
        db.execute("DELETE FROM users")
        users = {}
        for role in ("colaborador", "tecnico", "responsavel"):
            cursor = db.execute(
                "INSERT INTO users(name,email,secret,role) VALUES(?,?,?,?)",
                (role, role + "@test", hash_password("Password123!"), role))
            users[role] = {"id": cursor.lastrowid, "role": role}
        db.commit()
    yield users


def test_pg_create_read_update_across_connections(pg_users):
    """RF-002..RF-008, US-002..US-009: ciclo completo persiste após reconexão."""
    ana, miguel, sofia = (pg_users[k] for k in ("colaborador", "tecnico", "responsavel"))
    with connect() as db:
        ticket = services.create(db, ana, "Impressora", "Não imprime", "Equipamento")
        ticket_id = ticket["id"]
        assert ticket["state"] == "Aberto"
    with connect() as db:
        assert services.view(db, ana, ticket_id)["title"] == "Impressora"
        services.assign(db, sofia, ticket_id, miguel["id"])
        services.start(db, miguel, ticket_id)
        services.resolve(db, miguel, ticket_id, "Toner substituído")
    with connect() as db:
        saved = services.get(db, ticket_id)
        assert saved["state"] == "Resolvido"
        assert saved["resolution"] == "Toner substituído"
        services.reopen(db, ana, ticket_id)
        services.resolve(db, miguel, ticket_id, "Reparação concluída")
        services.close(db, sofia, ticket_id, True)
    with connect() as db:
        assert services.get(db, ticket_id)["state"] == "Fechado"


def test_pg_user_persists_across_connections(pg_users):
    """RF-001/US-001: utilizador permanece acessível após reconexão."""
    with connect() as db:
        row = db.execute("SELECT email,role FROM users WHERE id=?", (pg_users["colaborador"]["id"],)).fetchone()
        assert row["email"] == "colaborador@test"
        assert row["role"] == "colaborador"


def test_pg_http_login_create_and_read(pg_users):
    """RF-001/002/003, US-001/002/003: login, criação e listagem HTTP reais."""
    from fastapi.testclient import TestClient
    from src.main import create_app
    with TestClient(create_app(secret="test-secret-of-at-least-32-characters")) as client:
        response = client.post("/login", data={"email": "colaborador@test",
                                               "password": "Password123!"},
                               follow_redirects=False)
        assert response.status_code == 303
        created = client.post("/tickets/new", data={"title": "Monitor",
                                                     "description": "Sem imagem",
                                                     "category": "Equipamento"},
                              follow_redirects=False)
        assert created.status_code == 303
        assert "Monitor" in client.get("/tickets").text
