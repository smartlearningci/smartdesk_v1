"""RF/US: verificação de rastreabilidade dos cenários Gherkin aprovados.

A verificação de presença NÃO equivale à execução dos passos BDD. Os passos
em português serão ligados à implementação numa etapa de validação posterior.
"""
from pathlib import Path

def test_bdd_identifiers_present():
    """US-001 a US-012: esperado — nenhum identificador desapareceu."""
    feature = (Path(__file__).resolve().parents[1] / "features" / "tickets.feature").read_text()
    for number in range(1, 13):
        assert f"US-{number:03d}" in feature
