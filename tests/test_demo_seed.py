import sqlite3

import pytest

from src.database import initialize
from src.demo_seed import seed_demo_users
from src.auth import verify


def test_seed_cria_tres_contas_uma_vez():
    db = sqlite3.connect(":memory:")
    db.row_factory = sqlite3.Row
    initialize(db)

    assert seed_demo_users(db, "password-lab-123") == 3
    assert seed_demo_users(db, "password-lab-123") == 0

    users = db.execute("SELECT * FROM users ORDER BY email").fetchall()
    assert len(users) == 3
    assert all(verify("password-lab-123", u["secret"]) for u in users)
    assert all(u["secret"] != "password-lab-123" for u in users)
    db.close()


def test_seed_rejeita_password_curta():
    db = sqlite3.connect(":memory:")
    initialize(db)
    with pytest.raises(ValueError):
        seed_demo_users(db, "123")
    db.close()