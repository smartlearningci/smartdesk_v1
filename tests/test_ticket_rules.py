"""RF-002/005/006/007/008, US-002/006/007/008/009/010, T-02/06/07/08/09/10/15/19/20.

Esperado: ciclo de vida completo, solução persistida, estados protegidos,
campos obrigatórios e categorias validadas.
"""
import pytest
from fastapi import HTTPException
from src.database import connect
from src import services
from .conftest import person, create_ticket

def test_t02_t06_t07_t08_t09_t15_t20_lifecycle(env):
    _, path = env
    with connect(path) as db:
        ana, miguel, sofia = (person(db, email) for email in
                             ("ana@test", "miguel@test", "sofia@test"))
        ticket = create_ticket(db)
        assert ticket["state"] == "Aberto"
        services.assign(db, sofia, ticket["id"], miguel["id"])
        assert services.start(db, miguel, ticket["id"])["state"] == "Em tratamento"
        resolved = services.resolve(db, miguel, ticket["id"], "Substituído toner")
        assert resolved["state"] == "Resolvido"
        assert resolved["resolution"] == "Substituído toner"
        returned = services.reopen(db, ana, ticket["id"])
        assert returned["state"] == "Em tratamento"
        assert returned["technician_id"] == miguel["id"]
        services.resolve(db, miguel, ticket["id"], "Reparação concluída")
        with pytest.raises(HTTPException):
            services.close(db, sofia, ticket["id"], False)
        assert services.close(db, sofia, ticket["id"], True)["state"] == "Fechado"
        with pytest.raises(HTTPException):
            services.reopen(db, ana, ticket["id"])

@pytest.mark.parametrize("title,description,category,fragment", [
    ("", "Problema", "Equipamento", "título"),
    ("Pedido", "", "Equipamento", "descrição"),
    ("Pedido", "Problema", "", "categoria"),
    ("Pedido", "Problema", "Outra", "categoria"),
])
def test_t10_t19_invalid_ticket_fields(env, title, description, category, fragment):
    _, path = env
    with connect(path) as db:
        with pytest.raises(HTTPException) as exc:
            services.create(db, person(db, "ana@test"), title, description, category)
        assert fragment in str(exc.value.detail).lower()

@pytest.mark.parametrize("category", services.CATEGORIES)
def test_t19_all_categories_allowed(env, category):
    _, path = env
    with connect(path) as db:
        ticket = services.create(db, person(db, "ana@test"), "Pedido", "Problema", category)
        assert ticket["category"] == category
