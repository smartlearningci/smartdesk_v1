"""Executa os conjuntos pytest e gera JUnit XML, HTML e resumo global.

Os cenários Gherkin não automatizados e os ensaios manuais nunca são aprovados
por inferência. Os relatórios refletem apenas resultados efetivamente recolhidos.
"""
import html
import json
import subprocess
import sys
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "reports"
SUITES = {
    "unitarios": ["tests/test_ticket_rules.py", "tests/test_permissions.py", "tests/test_mvp.py"],
    "http": ["tests/test_api.py", "tests/test_auth.py", "tests/test_health.py"],
    "bdd": ["tests/test_bdd.py"],
    "postgres": ["tests/test_postgres.py"],
}
# Identificadores efetivamente relacionados com testes pytest existentes.
# Uma associação NÃO comprova cobertura integral do teste T documentado.
REFERENCES = {
    "unitarios": "T-02 a T-10, T-14 a T-20 (cobertura parcial por caso)",
    "http": "T-01 a T-04, T-06 a T-10, T-13 e /health (parcial)",
    "bdd": "Rastreabilidade US-001 a US-012; passos BDD NÃO executados",
    "postgres": "RF-001..RF-008; US-001..US-009; integração PostgreSQL, não reinício Docker",
}
CSS = """body{font:15px system-ui,sans-serif;max-width:1100px;margin:2rem auto;padding:0 1rem;color:#20252b}
table{border-collapse:collapse;width:100%;margin:1rem 0}td,th{padding:.65rem;border-bottom:1px solid #ddd;text-align:left;vertical-align:top}
th{background:#f2f3f5}.passed{color:#137333}.failed,.error{color:#b3261e}
.skipped{color:#a46b00}.not-run{color:#69717a}.pill{font-weight:bold}
pre{white-space:pre-wrap;overflow-wrap:anywhere;background:#f5f5f5;padding:1rem}
a{color:#1557a0}"""
LABELS = {"passed": "Aprovado", "failed": "Falhou", "error": "Erro",
          "skipped": "Ignorado", "not-run": "Não executado"}

def page(title, body):
    return ("<!doctype html><html lang='pt'><meta charset='utf-8'>"
            "<meta name='viewport' content='width=device-width, initial-scale=1'>"
            f"<title>{html.escape(title)}</title><style>{CSS}</style>"
            f"<body><h1>{html.escape(title)}</h1>{body}</body></html>")

def inspect_xml(path):
    if not path.exists():
        return [], "Ficheiro JUnit não foi produzido."
    try:
        tree = ET.parse(path)
        cases = []
        for node in tree.iter("testcase"):
            result = "passed"
            detail = ""
            for tag, state in (("failure", "failed"), ("error", "error"), ("skipped", "skipped")):
                found = node.find(tag)
                if found is not None:
                    result = state
                    detail = found.get("message", "") + "\n" + (found.text or "")
                    break
            cases.append({"name": node.get("name", ""), "classname": node.get("classname", ""),
                          "time": node.get("time", ""), "status": result, "detail": detail})
        return cases, None
    except (ET.ParseError, OSError) as exc:
        return [], f"JUnit inválido: {exc}"

def suite_html(name, cases, error, returncode):
    counts = Counter(c["status"] for c in cases)
    rows = "".join(
        f"<tr><td>{html.escape(c['classname'] + '::' + c['name'])}</td>"
        f"<td class='{c['status']} pill'>{LABELS[c['status']]}</td>"
        f"<td>{html.escape(c['time'])} s</td></tr>"
        + (f"<tr><td colspan='3'><pre>{html.escape(c['detail'])}</pre></td></tr>" if c["detail"] else "")
        for c in cases
    )
    info = f"<p>Referências: {html.escape(REFERENCES[name])}</p>"
    info += f"<p>Processo pytest: código de saída {returncode}.</p>"
    info += "<p>" + " · ".join(f"{LABELS[s]}: {counts[s]}" for s in ("passed","failed","error","skipped")) + "</p>"
    if error:
        info += f"<p class='error'>{html.escape(error)}</p>"
    if not cases:
        info += "<p class='not-run'>Nenhum caso com resultado JUnit: não executado / não comprovado.</p>"
    return page("SmartDesk — " + name, info + "<table><tr><th>Teste pytest</th><th>Estado</th><th>Tempo</th></tr>" + rows + "</table>")

def main():
    OUT.mkdir(parents=True, exist_ok=True)
    results = {}
    for name, files in SUITES.items():
        xml = OUT / (name + ".xml")
        if xml.exists():
            xml.unlink()  # Nunca reutilizar resultados antigos como se fossem atuais.
        command = [sys.executable, "-m", "pytest", "-q", "--junitxml=" + str(xml), *files]
        try:
            proc = subprocess.run(command, cwd=ROOT, capture_output=True, text=True, check=False)
            rc, output = proc.returncode, proc.stdout + "\n" + proc.stderr
        except OSError as exc:
            rc, output = 127, str(exc)
        cases, error = inspect_xml(xml)
        counts = Counter(c["status"] for c in cases)
        if rc != 0 and not (counts["failed"] or counts["error"]):
            # Erro de recolha, infraestrutura ou ausência de casos; não fingir sucesso.
            error = (error + " " if error else "") + "pytest terminou sem sucesso: " + output[-3000:]
        (OUT / (name + ".html")).write_text(suite_html(name, cases, error, rc), encoding="utf-8")
        results[name] = {"exit_code": rc, "counts": {s: counts[s] for s in LABELS},
                         "collected": len(cases), "error": error,
                         "junit": name + ".xml" if xml.exists() else None,
                         "html": name + ".html"}
        print(f"{name}: {len(cases)} resultados, saída {rc}", flush=True)

    totals = Counter()
    for item in results.values():
        totals.update(item["counts"])
    # T-01..T-20 são a matriz de aceitação, não 20 casos pytest.
    # Sem execução individual e evidência integral, mantêm-se pendentes.
    planned = {f"T-{i:02d}": {"status": "not-run",
               "note": "Não existe evidência individual completa nesta execução automatizada"}
               for i in range(1, 21)}
    planned["T-11"]["note"] = "Medição de desempenho ainda não executada"
    planned["T-12"]["note"] = "Chrome e Edge ainda não ensaiados"
    bdd = {f"US-{i:03d}": "not-run" for i in range(1, 13)}
    summary = {"generated_at_utc": datetime.now(timezone.utc).isoformat(),
               "pytest": {"suites": results, "totals": {s: totals[s] for s in LABELS}},
               "acceptance_tests": planned, "gherkin_scenarios": bdd,
               "notes": ["Os testes pytest podem abranger partes de vários T.",
                         "BDD verifica apenas identificadores; não executa os passos.",
                         "T-11 e T-12 requerem ensaios próprios."]}
    (OUT / "relatorio_global.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")
    rows = "".join(
        f"<tr><td><a href='{name}.html'>{name}</a></td>"
        + "".join(f"<td>{r['counts'][s]}</td>" for s in ("passed","failed","error","skipped"))
        + f"<td>{r['exit_code']}</td></tr>" for name, r in results.items())
    body = "<p>Resultados reais do pytest; não confundir com os 20 testes T documentados.</p>"
    body += "<table><tr><th>Conjunto</th><th>Aprovados</th><th>Falhados</th><th>Erros</th><th>Ignorados</th><th>Saída</th></tr>" + rows
    body += "<tr><th>Total</th>" + "".join(f"<th>{totals[s]}</th>" for s in ("passed","failed","error","skipped")) + "<th>—</th></tr></table>"
    body += "<h2>Validação do MVP ainda pendente</h2>"
    body += "<p class='not-run'>T-01 a T-20: 20 verificações documentadas sem evidência individual integral consolidada neste relatório. "
    body += "Os casos pytest acima demonstram apenas as verificações concretas executadas.</p>"
    body += "<p class='not-run'>12 cenários US Gherkin: passos não automatizados. T-11: desempenho não medido. T-12: navegadores não ensaiados.</p>"
    body += "<p><a href='relatorio_global.json'>Dados globais JSON</a></p>"
    (OUT / "relatorio_global.html").write_text(page("SmartDesk — Relatório global", body), encoding="utf-8")
    print("Relatórios disponíveis em reports/relatorio_global.html", flush=True)
    return 1 if any(r["exit_code"] != 0 for r in results.values()) else 0

if __name__ == "__main__":
    raise SystemExit(main())
