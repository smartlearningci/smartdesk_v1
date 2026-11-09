"""Verificação técnica /health: endpoint HTTP do MVP containerizado.

Técnico (Docker/Compose); complementa RNF-002 (disponibilidade/resposta)
sem substituir a medição T-11 de desempenho nem a autenticação RNF-003.
"""
def test_health_returns_ok_without_login(env):
    client, _ = env
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}
