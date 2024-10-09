# Use uma imagem oficial do Python
FROM python:3.9-slim

# criar  um container

# Defina o diretório de trabalho no container
WORKDIR /app

# Copie o script para o container

#COPY hash_string.py .

COPY mascarar.py .

# Comando para executar o script

# primeira vez CMD ["python", "carguru.py"]

#segunda vez 

 CMD ["python", "mascarar.py"]


# resumo do processo
# listar containers: docker ps ou docker ps -a. todos se quiser so os em em execução é docker ps
# parar container: docker stop <container_id>.
# reiniciar container: docker start <container_id>.
# remover container: docker rm <container_id> (opcional).

# O -it permite a interação com o terminal dentro do container, permitindo que você forneça a entrada de texto quando o script pedir.


# CMD ["python", "hash_string.py"]: Esse comando no Dockerfile define o que será executado quando o container for iniciado. Ele executa python com o script hash_string.py.
# -it: A opção -it permite que o terminal do container seja interativo, o que é necessário para que o input() no script funcione corretamente.

# pagar
#docker rm <CONTAINER_ID>

# docker inspect <CONTAINER_ID>
# Isso exibirá informações JSON detalhadas sobre o container, incluindo informações de montagem


# docker logs 

# como fazer todar 

# docker run -it mascarar-dados

# docker run -it hash   

# docker run -it carguru-app 