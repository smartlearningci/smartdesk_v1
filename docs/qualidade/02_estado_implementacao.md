# Estado da implementação e evidências de teste

**Âmbito:** MVP SmartDesk aprovado, sem alteração de requisitos, User Stories, código da aplicação ou cenários Gherkin.

## Implementação

- Interface HTML: `src/templates/` e `src/static/style.css`.
- HTTP e formulários: `src/main.py`.
- Regras de negócio: `src/services.py`.
- Autenticação e sessões: `src/auth.py`.
- Persistência SQLite: `src/database.py`.
- Testes: `tests/`; execução por Docker Compose em serviço `tests`.
- Relatórios: pasta partilhada `reports/`, com JUnit XML, HTML e JSON global.

## Procedimento da demonstração local

Na pasta do projeto:

```bash
cp .env.example .env
docker compose build
docker compose run --rm -it app python -m scripts.create_demo_users
docker compose up -d
```

O ficheiro `.env.example` contém uma chave **fictícia exclusivamente para formação local**.
O script pede palavras-passe de pelo menos oito caracteres para as contas
`ana@nexaserv.test`, `miguel@nexaserv.test` e `sofia@nexaserv.test`.
Abrir `http://localhost:8080/login` e iniciar sessão com as credenciais escolhidas.

Para parar sem eliminar o volume SQLite:

```bash
docker compose down
```

## Execução de testes e relatórios

```bash
mkdir -p reports
docker compose build tests
docker compose run --rm tests
```

Em Linux, se necessário para permissões de escrita na pasta partilhada:

```bash
LOCAL_UID="$(id -u)" LOCAL_GID="$(id -g)" docker compose run --rm tests
```

Abrir `reports/relatorio_global.html`. O ficheiro `relatorio_global.json`
regista os resultados por conjunto. A base SQLite usada pelos testes é isolada
dos dados da demonstração.

## Evidência recebida — 9 de novembro de 2026

**Fonte:** ficheiro `relatorio_global.json` fornecido após a sessão,
gerado em `2026-11-09T15:26:03.848422+00:00`.

| Conjunto pytest | Aprovados | Falhados | Erros | Ignorados | Código de saída |
|---|---:|---:|---:|---:|---:|
| Unitários/regras | 12 | 0 | 0 | 0 | 0 |
| Integração HTTP | 5 | 0 | 0 | 0 | 0 |
| Verificação de identificadores BDD | 1 | 0 | 0 | 0 | 0 |
| **Total** | **18** | **0** | **0** | **0** | — |

**Validado pelo relatório:** 18 casos pytest concluíram com sucesso. O caso
`test_bdd.py` confirma identificadores de User Stories no ficheiro Gherkin,
**não** executa os passos Dado/Quando/Então.

**Sem evidência autónoma recebida:** sucesso do build Docker, criação das contas,
login manual, navegação e demonstração funcional no browser. Os comandos estão
documentados, mas o JSON não comprova essas ações.

## Aceitação e limitações

- **T-01 a T-20:** todos constam como `not-run` na matriz de aceitação do
  relatório, por não haver evidência individual integral consolidada. Isto
  **não anula** os 18 resultados pytest aprovados, que verificam partes dos
  requisitos.
- **Cenários Gherkin US-001 a US-012:** `not-run`; passos não automatizados.
- **T-11 / RNF-002:** medição de desempenho não executada.
- **T-12 / RNF-004:** ensaios reais em Chrome e Edge não executados.
- **Falhas observadas no pytest:** nenhuma reportada nos 18 casos executados.
  Não foram fornecidos registos de eventuais problemas da demonstração manual.
- **Segurança:** aplicação de formação local; formulários sem proteção CSRF
  e cookies sem HTTPS obrigatório. Não expor à Internet.

**Critério de reporte:** um teste só é considerado aprovado quando existe
resultado da sua execução. Ausência de evidência não equivale a aprovação.

## Próximos passos da formação

1. Registar, se disponíveis, evidências da demonstração manual e eventuais falhas.
2. Prosseguir com Docker, orquestração e CI/CD, reutilizando o MVP existente.
3. Numa etapa posterior, automatizar os passos BDD e preparar a medição T-11 e
   os ensaios T-12, sem alterar os requisitos aprovados.
