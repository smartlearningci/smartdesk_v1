"""RF-001, RNF-003: autenticação local e controlo de perfis.

PBKDF2-HMAC-SHA256 com sal aleatório e comparação constante.
O cookie de sessão é assinado pelo SessionMiddleware em main.py.
"""
import hashlib
import hmac
import secrets
from fastapi import HTTPException

def hash_password(password):
    salt = secrets.token_hex(16)
    digest = hashlib.pbkdf2_hmac("sha256", password.encode(),
                                 bytes.fromhex(salt), 310_000).hex()
    return salt + ":" + digest

def verify(password, encoded):
    try:
        salt, expected = encoded.split(":")
        digest = hashlib.pbkdf2_hmac("sha256", password.encode(),
                                     bytes.fromhex(salt), 310_000).hex()
        return hmac.compare_digest(digest, expected)
    except (ValueError, TypeError):
        return False

def current(request, db):
    user_id = request.session.get("uid")
    row = db.execute("SELECT id,name,email,role FROM users WHERE id=?",
                     (user_id,)).fetchone() if user_id else None
    if row is None:
        raise HTTPException(401, "É necessário iniciar sessão.")
    return dict(row)

def require(user, role):
    if user["role"] != role:
        raise HTTPException(403, "O seu perfil não permite esta operação.")
