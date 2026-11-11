"""Executa suites independentes e gera relatórios JUnit, HTML e resumo global.

Usar dentro do Docker Compose; nenhuma dependência Python local.
A saída da suite é preservada e falhas não impedem as suites seguintes.
"""
from pathlib import Path
import subprocess
import sys
from scripts.generate_report import generate

ROOT = Path(__file__).resolve().parents[1]
REPORTS = ROOT / "reports"
SUITES = {
    "unit": ["tests/test_ticket_rules.py", "tests/test_permissions.py", "tests/test_mvp.py"],
    "integration": ["tests/test_auth.py", "tests/test_api.py"],
    "bdd": ["tests/bdd/test_scenarios.py"],
    "postgres": ["tests/test_postgres.py"],
}

def main():
    REPORTS.mkdir(exist_ok=True)
    codes = {}
    for suite, paths in SUITES.items():
        folder = REPORTS / suite
        folder.mkdir(parents=True, exist_ok=True)
        cmd = [sys.executable, "-m", "pytest", "-v", *paths,
               f"--junitxml={folder / 'junit.xml'}",
               f"--html={folder / 'index.html'}", "--self-contained-html"]
        print(f"\n### {suite.upper()} ###", flush=True)
        codes[suite] = subprocess.run(cmd, cwd=ROOT, check=False).returncode
    generate(REPORTS, codes)
    print(f"\nRelatório global: {REPORTS / 'index.html'}", flush=True)
    # O relatório nunca converte falhas ou suites não executadas em sucesso.
    return 0 if all(code == 0 for code in codes.values()) else 1

if __name__ == "__main__":
    raise SystemExit(main())
