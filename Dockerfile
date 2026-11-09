# Imagem Python pequena e adequada ao MVP pedagógico.
FROM python:3.12-slim

# Os ficheiros do projeto ficam em /app.
WORKDIR /app

# Evita ficheiros .pyc e apresenta os logs sem atraso.
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Instala as dependências antes do código para aproveitar a cache do build.
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia apenas o que não estiver excluído em .dockerignore.
COPY . .

# O SQLite escreve num volume; a aplicação não precisa de root.
RUN useradd --system --uid 10001 --no-create-home smartdesk \
    && mkdir -p /data \
    && chown smartdesk:smartdesk /data
USER smartdesk

# Porta interna; a publicação no computador é definida no Compose.
EXPOSE 8000

# Importa a aplicação real declarada em src/main.py.
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]
