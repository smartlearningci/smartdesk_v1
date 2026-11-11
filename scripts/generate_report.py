"""Consolida os JUnit XML em HTML estático sem dependências adicionais.

Um teste só é 'aprovado' quando existe testcase executado sem falha/erro/skip.
Ausência de XML ou de testcase significa 'não executado', nunca 'aprovado'.
"""
from collections import Counter
from datetime import datetime, timezone
from html import escape
from pathlib import Path
import re
import xml.etree.ElementTree as ET

EXPECTED = {f"T-{n:02d}" for n in range(1, 21)}
SUITES = ("unit", "integration", "bdd", "postgres")
COLORS = {"aprovado": "#207343", "falhado": "#b42318",
          "erro": "#b42318", "ignorado": "#ad7700", "não executado": "#667085"}
T_RE = re.compile(r"(?<![A-Za-z0-9])t(\d{2})(?!\d)", re.I)

def parse(path):
    if not path.exists():
        return [], "XML ausente"
    try:
        root = ET.parse(path).getroot()
        cases = []
        for element in root.iter("testcase"):
            name = element.get("name", "")
            if element.find("error") is not None:
                status = "erro"
            elif element.find("failure") is not None:
                status = "falhado"
            elif element.find("skipped") is not None:
                status = "ignorado"
            else:
                status = "aprovado"
            cases.append((element.get("classname", ""), name, status,
                          element.get("time", "0")))
        return cases, None
    except (ET.ParseError, OSError) as exc:
        return [], str(exc)

def cell(status):
    return f'<span class="status" style="color:{COLORS[status]}">{escape(status)}</span>'

def generate(folder, exit_codes=None):
    exit_codes = exit_codes or {}
    all_cases, rows = [], []
    for suite in SUITES:
        cases, problem = parse(folder / suite / "junit.xml")
        all_cases.extend((suite, *case) for case in cases)
        counts = Counter(case[2] for case in cases)
        counts["não executado"] = int(problem is not None)
        status = f"código {exit_codes[suite]}" if suite in exit_codes else "não informado"
        rows.append((suite, counts, status, problem))

    totals = Counter(case[3] for case in all_cases)
    totals["não executado"] = sum(bool(problem) for _, _, _, problem in rows)
    # Um ID T-xx pode ter várias verificações; nunca somar IDs como testes.
    ids = {key: [] for key in EXPECTED}
    for suite, classname, name, status, _ in all_cases:
        for match in T_RE.findall(name):
            key = f"T-{match}"
            if key in ids:
                ids[key].append((suite, status))
    def id_status(items):
        if not items:
            return "não executado"
        statuses = {status for _, status in items}
        if "erro" in statuses: return "erro"
        if "falhado" in statuses: return "falhado"
        if "ignorado" in statuses: return "não executado" if statuses == {"ignorado"} else "ignorado"
        return "aprovado"

    css = """body{font:15px system-ui,sans-serif;max-width:1100px;margin:2rem auto;padding:0 1rem;color:#243448}
    table{border-collapse:collapse;width:100%;margin:1rem 0}th,td{padding:.6rem;text-align:left;border-bottom:1px solid #ddd}
    .status{font-weight:700}.cards{display:flex;gap:.8rem;flex-wrap:wrap}.card{border:1px solid #ddd;border-radius:8px;padding:1rem;min-width:125px}
    .card strong{display:block;font-size:1.5rem}a{color:#165d9b}"""
    html = ['<!doctype html><html lang="pt"><meta charset="utf-8"><title>SmartDesk — Validação</title>',
            f"<style>{css}</style><h1>SmartDesk — Relatório global</h1>",
            f"<p>Gerado em {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')}. "
            "Aprovação exige execução real; ignorados e não executados não são aprovados.</p>",
            '<h2>Totais de casos de teste</h2><div class="cards">']
    for key in ("aprovado", "falhado", "erro", "ignorado", "não executado"):
        html.append(f'<div class="card">{cell(key)}<strong>{totals[key]}</strong></div>')
    html.append('</div><p>Não executado no total acima: suites sem XML válido. '
                'IDs de aceitação não cobertos aparecem separadamente abaixo.</p>')
    html.append('<h2>Por conjunto</h2><table><tr><th>Conjunto</th><th>Aprovados</th><th>Falhados</th><th>Erros</th><th>Ignorados</th><th>Não executados*</th><th>Saída</th><th>Relatórios</th></tr>')
    for suite, counts, code, problem in rows:
        html.append(f'<tr><td>{escape(suite)}</td>'
                    + ''.join(f'<td>{counts[k]}</td>' for k in ("aprovado", "falhado", "erro", "ignorado", "não executado"))
                    + f'<td>{escape(code)}{": "+escape(problem) if problem else ""}</td>'
                    + f'<td><a href="{suite}/index.html">HTML</a> · <a href="{suite}/junit.xml">JUnit XML</a></td></tr>')
    html.append('</table><p>*Contagem de conjuntos sem XML, não número de casos desconhecidos.</p>')
    html.append('<h2>Rastreabilidade T-01 a T-20</h2><table><tr><th>ID</th><th>Estado observado</th><th>Conjuntos com casos identificados</th></tr>')
    for key in sorted(EXPECTED):
        items = ids[key]
        html.append(f'<tr><td>{key}</td><td>{cell(id_status(items))}</td>'
                    f'<td>{escape(", ".join(sorted(set(suite for suite, _ in items))) or "sem caso identificado")}</td></tr>')
    html.append('</table><p>O estado por ID é um indicador dos casos encontrados pelo nome, '
                'não uma certificação de cobertura integral dos critérios de aceitação.</p></html>')
    (folder / "index.html").write_text("\n".join(html), encoding="utf-8")
    return totals

if __name__ == "__main__":
    generate(Path("reports"))
