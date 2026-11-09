"""RF-003/004/005/008/009, US-003/004/005/006/009, T-03/04/05/14/16/17/18.

Esperado: visibilidade por perfil; só Sofia atribui e fecha; reatribuição
não altera o estado; um técnico não altera tickets alheios.
"""
import pytest
from fastapi import HTTPException
from src.database import connect
from src import services
from .conftest import person, create_ticket

def test_t03_t05_t18_visibility(env):
    _, path = env
    with connect(path) as db:
        ana = person(db, "ana@test")
        other = person(db, "outro@test")
        miguel = person(db, "miguel@test")
        sofia = person(db, "sofia@test")
        ticket = create_ticket(db)
        assert len(services.listing(db, ana)) == 1
        assert services.listing(db, other) == []
        assert services.listing(db, miguel) == []
        assert len(services.listing(db, sofia)) == 1
        with pytest.raises(HTTPException) as exc:
            services.view(db, other, ticket["id"])
        assert exc.value.status_code == 403

def test_t04_t16_reassignment_keeps_state(env):
    _, path = env
    with connect(path) as db:
        sofia = person(db, "sofia@test")
        miguel = person(db, "miguel@test")
        other_tech = person(db, "tecnico2@test")
        ticket = create_ticket(db)
        ticket = services.assign(db, sofia, ticket["id"], miguel["id"])
        assert ticket["state"] == "Aberto"
        services.start(db, miguel, ticket["id"])
        ticket = services.assign(db, sofia, ticket["id"], other_tech["id"])
        assert ticket["state"] == "Em tratamento"
        assert ticket["technician_id"] == other_tech["id"]

def test_t14_t17_unauthorized_operations(env):
    _, path = env
    with connect(path) as db:
        miguel = person(db, "miguel@test")
        other_tech = person(db, "tecnico2@test")
        sofia = person(db, "sofia@test")
        ticket = create_ticket(db)
        services.assign(db, sofia, ticket["id"], miguel["id"])
        with pytest.raises(HTTPException) as exc:
            services.start(db, other_tech, ticket["id"])
        assert exc.value.status_code == 403
        with pytest.raises(HTTPException) as exc:
            services.close(db, miguel, ticket["id"], True)
        assert exc.value.status_code == 403
