"""Armazenamento SQLite (arquitetura aprovada).

A ligação tem foreign_keys ativadas. CHECK protege estados e categorias,
mesmo quando uma escrita não passa pelos formulários HTML.
"""
import os
import sqlite3

def connect(path=None):
    db = sqlite3.connect(path or os.getenv("SMARTDESK_DB", "smartdesk.sqlite3"))
    db.row_factory = sqlite3.Row
    db.execute("PRAGMA foreign_keys=ON")
    return db

def initialize(db):
    """Cria apenas as tabelas inexistentes; não apaga tickets existentes."""
    db.executescript("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        email TEXT NOT NULL UNIQUE,
        secret TEXT NOT NULL,
        role TEXT NOT NULL CHECK(role IN ('colaborador','tecnico','responsavel'))
    );
    CREATE TABLE IF NOT EXISTS tickets (
        id INTEGER PRIMARY KEY,
        title TEXT NOT NULL CHECK(length(trim(title)) > 0),
        description TEXT NOT NULL CHECK(length(trim(description)) > 0),
        category TEXT NOT NULL CHECK(category IN ('Equipamento','Software','Acessos')),
        state TEXT NOT NULL DEFAULT 'Aberto'
          CHECK(state IN ('Aberto','Em tratamento','Resolvido','Fechado')),
        creator_id INTEGER NOT NULL REFERENCES users(id),
        technician_id INTEGER REFERENCES users(id),
        resolution TEXT
    );
    """)
    db.commit()
