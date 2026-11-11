"""Inicialização idempotente de contas fictícias do SmartDesk (laboratório)."""

from src.auth import hash_password

DEMO_USERS = (
    ("Ana Martins", "ana@nexaserv.test", "colaborador"),
    ("Miguel Costa", "miguel@nexaserv.test", "tecnico"),
    ("Sofia Almeida", "sofia@nexaserv.test", "responsavel"),
)


def seed_demo_users(db, password: str) -> int:
    """Cria apenas utilizadores em falta. Devolve o número criado."""
    if not password or len(password) < 8:
        raise ValueError("SMARTDESK_DEMO_PASSWORD exige pelo menos 8 caracteres")

    created = 0
    for name, email, role in DEMO_USERS:
        found = db.execute(
            "SELECT id FROM users WHERE email=?", (email,)
        ).fetchone()
        if found is not None:
            continue
        db.execute(
            "INSERT INTO users(name,email,secret,role) VALUES(?,?,?,?)",
            (name, email, hash_password(password), role),
        )
        created += 1
    db.commit()
    return created