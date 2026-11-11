"""Integração PostgreSQL em esquema temporário isolado da aplicação."""
import os
import uuid
import pytest
from src.database import connect, initialize
from src import services
from src.auth import hash_password

@pytest.fixture
def pg_db():
    if not os.getenv("DATABASE_URL"):
        pytest.skip("DATABASE_URL ausente: PostgreSQL não executado")
    import psycopg
    from psycopg import sql
    schema = "smartdesk_test_" + uuid.uuid4().hex
    with psycopg.connect(os.environ["DATABASE_URL"], autocommit=True) as admin:
        admin.execute(sql.SQL("CREATE SCHEMA {}").format(sql.Identifier(schema)))
    db = None
    try:
        db = connect()
        db.connection.execute(sql.SQL("SET search_path TO {}").format(sql.Identifier(schema)))
        db.schema = schema
        initialize(db)
        yield db
    finally:
        if db:
            db.connection.close()
        with psycopg.connect(os.environ["DATABASE_URL"], autocommit=True) as admin:
            admin.execute(sql.SQL("DROP SCHEMA {} CASCADE").format(sql.Identifier(schema)))

def seed(db):
    people = []
    for role in ("colaborador", "tecnico", "responsavel"):
        result = db.execute("INSERT INTO users(name,email,secret,role) VALUES(?,?,?,?)",
                            (role, role + "@pg.test", hash_password("Password123!"), role))
        people.append({"id": result.lastrowid, "role": role})
    db.commit()
    return people

def test_pg01_pg06_initialization_is_idempotent(pg_db):
    ana, _, _ = seed(pg_db)
    ticket = services.create(pg_db, ana, "Impressora", "Não imprime", "Equipamento")
    initialize(pg_db)
    assert services.get(pg_db, ticket["id"])["title"] == "Impressora"

def test_pg02_pg03_pg04_pg05_pg08_lifecycle_and_new_connection(pg_db):
    ana, miguel, sofia = seed(pg_db)
    ticket = services.create(pg_db, ana, "Rede", "Sem acesso", "Acessos")
    ticket_id = ticket["id"]
    assert ticket["state"] == "Aberto"
    services.assign(pg_db, sofia, ticket_id, miguel["id"])
    assert services.start(pg_db, miguel, ticket_id)["state"] == "Em tratamento"
    assert services.resolve(pg_db, miguel, ticket_id, "Reconfigurado")["resolution"] == "Reconfigurado"
    assert services.close(pg_db, sofia, ticket_id, True)["state"] == "Fechado"
    from fastapi import HTTPException
    with pytest.raises(HTTPException):
        services.reopen(pg_db, ana, ticket_id)
    pg_db.commit()
    # Abrir outra ligação real à BD, sem usar o objeto original.
    from psycopg import sql
    with connect() as another:
        another.connection.execute(sql.SQL("SET search_path TO {}").format(sql.Identifier(pg_db.schema)))
        assert another.execute("SELECT state FROM tickets WHERE id=?", (ticket_id,)).fetchone()["state"] == "Fechado"
