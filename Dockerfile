# Imagem Python pequena, adequada ao laboratório local.
FROM python:3.12-slim

# Diretório de trabalho da aplicação dentro do contentor.
WORKDIR /app

# Instalar primeiro as dependências para aproveitar a cache de build.
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar a aplicação, os testes e os scripts de demonstração.
# O .dockerignore exclui segredos e ficheiros locais.
COPY . .

# O serviço recebe ligações dentro da rede Docker nesta porta.
EXPOSE 8000

# Sem --reload: uma única aplicação web por contentor.
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]
