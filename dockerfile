# Usa imagem base com Python 3.10
FROM python:3.10-slim

# Instala o Git e outras dependências
RUN apt-get update && \
    apt-get install -y git && \
    apt-get clean

# Cria diretório da aplicação
WORKDIR /app

# Copia todos os arquivos da pasta atual para o container
COPY . /app

# Instala as dependências do projeto (se houver requirements.txt)
RUN pip install --no-cache-dir streamlit

# Comando default (pode ser alterado depois)
CMD [ "bash" ]
