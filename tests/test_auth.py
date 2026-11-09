"""RF-001/RNF-003, US-001, T-01/T-13: autenticação e sessão.

Esperado: credenciais corretas permitem consultar tickets; incorretas
não autenticam; sair invalida a sessão.
"""
from .conftest import login

def test_t01_valid_login_and_logout(env):
    client, _ = env
    login(client, "ana@test")
    assert client.get("/tickets").status_code == 200
    assert client.post("/logout", follow_redirects=False).status_code == 303
    assert client.get("/tickets", follow_redirects=False).status_code == 303

def test_t13_wrong_password(env):
    client, _ = env
    response = client.post("/login", data={"email": "ana@test", "password": "errada"})
    assert "incorretos" in response.text
    assert client.get("/tickets", follow_redirects=False).status_code == 303
