"""RF-001/002/003/004/005/006/007/008/009, US-002/003/004/006/007/008/009/010.

Integração HTTP: os formulários chamam a mesma camada de regras usada
nos testes unitários. Esperado: redirecionamentos 303 e SQLite persistente.
"""
from .conftest import login, person
from src.database import connect

def test_t02_t03_t10_http_creation_visibility_and_validation(env):
    client, path = env
    login(client, "ana@test")
    response = client.post("/tickets/new",
                           data={"title": "Impressora", "description": "Não imprime",
                                 "category": "Equipamento"}, follow_redirects=False)
    assert response.status_code == 303
    assert "Impressora" in client.get("/tickets").text
    error = client.post("/tickets/new", data={"title": "", "description": "Problema",
                                              "category": "Equipamento"})
    assert "título é obrigatório" in error.text
    client.post("/logout")
    login(client, "outro@test")
    assert "Impressora" not in client.get("/tickets").text
    with connect(path) as db:
        ticket_id = db.execute("SELECT id FROM tickets").fetchone()["id"]
    assert client.get(f"/tickets/{ticket_id}").status_code == 403

def test_t04_t06_t07_t08_t09_http_full_cycle(env):
    client, path = env
    login(client, "ana@test")
    client.post("/tickets/new", data={"title": "Impressora", "description": "Falha",
                                       "category": "Equipamento"})
    with connect(path) as db:
        ticket_id = db.execute("SELECT id FROM tickets").fetchone()["id"]
        tech_id = person(db, "miguel@test")["id"]
    client.post("/logout")
    login(client, "sofia@test")
    assert client.post(f"/api/tickets/{ticket_id}/assign",
                       data={"technician_id": tech_id}, follow_redirects=False).status_code == 303
    client.post("/logout")
    login(client, "miguel@test")
    assert client.post(f"/api/tickets/{ticket_id}/start", follow_redirects=False).status_code == 303
    assert client.post(f"/api/tickets/{ticket_id}/resolve",
                       data={"resolution": "Reparado"}, follow_redirects=False).status_code == 303
    client.post("/logout")
    login(client, "ana@test")
    assert client.post(f"/api/tickets/{ticket_id}/return", follow_redirects=False).status_code == 303
    client.post("/logout")
    login(client, "miguel@test")
    client.post(f"/api/tickets/{ticket_id}/resolve", data={"resolution": "Resolvido"})
    client.post("/logout")
    login(client, "sofia@test")
    assert client.post(f"/api/tickets/{ticket_id}/close",
                       data={"confirmed": "true"}, follow_redirects=False).status_code == 303
    with connect(path) as db:
        assert db.execute("SELECT state FROM tickets WHERE id=?", (ticket_id,)).fetchone()["state"] == "Fechado"
