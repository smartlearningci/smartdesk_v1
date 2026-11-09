"""Regras do MVP, independentes da interface HTML.

RF-002/US-002,010: criação e validação;
RF-003/US-003,005: visibilidade;
RF-004/US-004: atribuição e reatribuição;
RF-005/US-006: tratamento; RF-006/US-007: resolução;
RF-007/US-008: regresso; RF-008/US-009: fecho;
RF-009/US-009: supervisão.
"""
from fastapi import HTTPException
from .auth import require
CATEGORIES = ("Equipamento", "Software", "Acessos")

def error(message, status=400):
    raise HTTPException(status_code=status, detail=message)

def get(db, ticket_id):
    row = db.execute("SELECT * FROM tickets WHERE id=?", (ticket_id,)).fetchone()
    if row is None:
        error("O ticket solicitado não existe.", 404)
    return dict(row)

def allowed(user, ticket):
    """A responsável vê todos; os restantes apenas os tickets autorizados."""
    return (user["role"] == "responsavel"
            or (user["role"] == "colaborador" and ticket["creator_id"] == user["id"])
            or (user["role"] == "tecnico" and ticket["technician_id"] == user["id"]))

def view(db, user, ticket_id):
    ticket = get(db, ticket_id)
    if not allowed(user, ticket):
        error("Não tem autorização para consultar este ticket.", 403)
    return ticket

def listing(db, user):
    if user["role"] == "responsavel":
        rows = db.execute("SELECT * FROM tickets ORDER BY id DESC")
    elif user["role"] == "tecnico":
        rows = db.execute("SELECT * FROM tickets WHERE technician_id=? ORDER BY id DESC", (user["id"],))
    else:
        rows = db.execute("SELECT * FROM tickets WHERE creator_id=? ORDER BY id DESC", (user["id"],))
    return [dict(row) for row in rows]

def create(db, user, title, description, category):
    require(user, "colaborador")
    if not title.strip():
        error("O título é obrigatório.")
    if not description.strip():
        error("A descrição é obrigatória.")
    if category not in CATEGORIES:
        error("Selecione uma categoria válida: Equipamento, Software ou Acessos.")
    cursor = db.execute(
        "INSERT INTO tickets(title,description,category,creator_id) VALUES(?,?,?,?)",
        (title.strip(), description.strip(), category, user["id"]))
    db.commit()
    return get(db, cursor.lastrowid)

def assign(db, user, ticket_id, technician_id):
    require(user, "responsavel")
    ticket = get(db, ticket_id)
    if ticket["state"] not in ("Aberto", "Em tratamento"):
        error("A atribuição só é permitida em Aberto ou Em tratamento.")
    row = db.execute("SELECT role FROM users WHERE id=?", (technician_id,)).fetchone()
    if not row or row["role"] != "tecnico":
        error("Selecione um técnico válido.")
    db.execute("UPDATE tickets SET technician_id=? WHERE id=?", (technician_id, ticket_id))
    db.commit()
    return get(db, ticket_id)

def assigned(db, user, ticket_id, state):
    require(user, "tecnico")
    ticket = get(db, ticket_id)
    if ticket["technician_id"] != user["id"]:
        error("Este ticket está atribuído a outro técnico.", 403)
    if ticket["state"] != state:
        error(f"Operação indisponível: o ticket não está no estado {state}.")

def start(db, user, ticket_id):
    assigned(db, user, ticket_id, "Aberto")
    db.execute("UPDATE tickets SET state='Em tratamento' WHERE id=?", (ticket_id,))
    db.commit()
    return get(db, ticket_id)

def resolve(db, user, ticket_id, solution):
    assigned(db, user, ticket_id, "Em tratamento")
    if not solution.strip():
        error("Registe a solução antes de resolver o ticket.")
    db.execute("UPDATE tickets SET state='Resolvido',resolution=? WHERE id=?",
               (solution.strip(), ticket_id))
    db.commit()
    return get(db, ticket_id)

def reopen(db, user, ticket_id):
    require(user, "colaborador")
    ticket = get(db, ticket_id)
    if ticket["creator_id"] != user["id"]:
        error("Não pode alterar tickets de outros colaboradores.", 403)
    if ticket["state"] != "Resolvido":
        error("Apenas tickets Resolvidos podem regressar a Em tratamento.")
    db.execute("UPDATE tickets SET state='Em tratamento' WHERE id=?", (ticket_id,))
    db.commit()
    return get(db, ticket_id)

def close(db, user, ticket_id, confirmed):
    require(user, "responsavel")
    ticket = get(db, ticket_id)
    if ticket["state"] != "Resolvido":
        error("Apenas tickets Resolvidos podem ser fechados.")
    if not confirmed:
        error("Confirme que verificou a resolução antes de fechar.")
    db.execute("UPDATE tickets SET state='Fechado' WHERE id=?", (ticket_id,))
    db.commit()
    return get(db, ticket_id)
