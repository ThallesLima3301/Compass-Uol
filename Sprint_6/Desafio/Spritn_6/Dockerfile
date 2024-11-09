# Use uma imagem base do Python
FROM python:3.9

# Defina o diretório de trabalho dentro do container
WORKDIR /app

# Copie o arquivo de requisitos primeiro para aproveitar o cache do Docker se ele não mudar
COPY requirements.txt /app

# Instale as bibliotecas necessárias a partir do requirements.txt
RUN pip install -r requirements.txt 

RUN apt-get update && apt-get install -y libglib2.0-0 libsm6 libxext6 libxrender-dev

# Copie todos os arquivos da pasta local para o diretório de trabalho do container
COPY . /app

# Comando para executar o script
CMD ["python", "s3_operations.py"]

# docker build -t ingestao-filmes-series .
#docker build --no-cache -t ingestao-filmes-series .
# docker run --env-file .env ingestao-filmes-series
# docker run -it ingestao-filmes-series /bin/bash
# docker run --env-file .env -it -v ${PWD}/gráficos:/app/notaComediaanimacao ingestao-filmes-series /bin/bash
# python notas.py 
