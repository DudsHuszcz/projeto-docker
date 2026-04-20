# Usa uma imagem oficial do Python mais leve
FROM python:3.9-slim

# Define a pasta de trabalho dentro do container
WORKDIR /app

# Copia o arquivo de dependências e instala
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia o resto do código para dentro do container
COPY . .

# Expõe a porta que a aplicação vai usar
EXPOSE 8080

# Comando para rodar a aplicação
CMD ["python", "app.py"]
