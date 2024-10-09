# Desafio da Sprint 

![enunciado](../evidencias/Desafio/enunciado/Desafio_enunciado1.png)

Vamos começar 

mas aneste disso vamo fazer um lista de comando importantes.

comandos usados para criar  
`docker build -t carguru-container .`
`docker build -t carguru-app .`
`docker build -t hash-app .`
` docker build -t mascarar-dados .`
rodar 
`docker run carguru-app`
`docker run -it hash-app .`
`docker run -it hash`
`docker run -it mascarar-dados`

romando uteis

`clear`
`docker images`
`docker ps -a`
`docker stop `
`docker logs `
`docker rm $(docker ps -a -q)`
`docker rm `


Baixar o arquivo CSV (carguru.py)

Criei um ambiente de trabalho usando Docker. 

Configuração do Dockerfile para Executar Scripts Python

Criação do Dockerfile:

![](../evidencias/Desafio/enunciado/Desafio_enunciado2.png)

O primeiro passo foi criar um Dockerfile para configurar e construir a imagem Docker que executaria os scripts Python.
Conteúdo inicial do Dockerfile:

eu Usei a versão python:3.9-slim mas fiz tambem usando 3.11-slim.

![](../evidencias/Desafio/resultados/Desafio_resultados_1.png)

Construção da Imagem com carguru.py:


No terminal, dentro do diretório onde estão os arquivos Dockerfile e carguru.py, o comando abaixo foi utilizado para construir a imagem:

`docker build -t carguru-container .`

Esse comando criará uma imagem chamada carguru-image com base no Dockerfile.

Execute o container criado a partir da imagem:

`docker run -it carguru-container`

![](../evidencias/Desafio/resultados/Desafio_resultados_2.png)

beleza tudo certo meu codigo esta rodando e me retornando qual carro eu dirijo 

mas antes disso vale resaltar que eu usei o comando `docker rm $(docker ps -a -q)` para limpar tudo e deixar mais claro pra vc


![](../evidencias/Desafio/resultados/Desafio_resultados_3.png)

agora vamos responder a etapa 2

Sim, é possível reutilizar containers no Docker. Quando um container está parado (ou seja, foi interrompido, mas ainda existe), ele pode ser reiniciado com o comando certo.

Para reiniciar um container parado, eu vou utilizar o seguinte comando:

`docker start b2e8f6fbed57`

![](../evidencias/Desafio/resultados/Desafio_resultados_4.png)

beleza confirmando que esta sendo reutilizado.

![](../evidencias/Desafio/resultados/Desafio_resultados_5.png)

optei por mudar o nome.

![](../evidencias/Desafio/resultados/Desafio_resultados_6.png)

usei o comando `docker run -d --name meu_container carguru-app`

Beleza vamos para etapa 3 que é crar um hash.

Primeiro eu crie um novo aquivo chamado "hash_string.py"


![](../evidencias/Desafio/resultados/Desafio_resultados_7.png)

Script Python para a etapa 3:

Crie um arquivo chamado hash_generator.py com o seguinte conteúdo:

peguei a primeira biblioteca que apreceu do google e por sorte deu certo de primeira
Para permitir a entrada de dados pelo usuário durante a execução do container, eu criei um novo script que receba um valor de entrada e execute o algoritmo SHA-1.

ficando assim eu aquivo  Dockerfile 

![](../evidencias/Desafio/resultados/Desafio_resultados_8.png)

agora vamos motrar o hash funcionando.

![](../evidencias/Desafio/resultados/Desafio_resultados_9.png)

**Nota: eu não sabia oque era um hash mas pesquisando um pouco parece que esta certo(depois confimei com o monitor)**

`docker images`

para mostrar como que esta.

![](../evidencias/Desafio/resultados/Desafio_resultados_10.png)

beleza falta mascarar os dados agora que é a ultima parte do desafio

![](../evidencias/Desafio/enunciado/Desafio_enunciado3.png)

fiz de 2 jeitos:

Jeito 1, esse é o jeito que sera documentado com evidencias, minha ideia foi criar um aquivo novo igual eu fiz com o hash.

Jeito 2, eu gostei mais de forma que eu  fiz onde eu crio um menu e deixo o usario escolher se ele quere mascarar dados ou um hash 

mas vamos focar no Jeito um aqui

![](../evidencias/Desafio/resultados/Desafio_resultados_11.png)

O código recebe um texto do usuário, substitui todas as vogais (a, e, i, o, u) por *, e imprime o texto resultante. É uma função útil para esconder certas partes de um texto, como em processos de anonimização de dados ou censura de palavras.

**Nota: eu sei que eu não fui criativo mas eu pensei em varias coisas e nenhuma ficou legal entao optei pelo basico mesmo**

ficando assim eu aquivo  Dockerfile 

![](../evidencias/Desafio/resultados/Desafio_resultados_12.png)

entao vamos la fazer os testes

![](../evidencias/Desafio/resultados/Desafio_resultados_13.png)

beleza deu tudo certo.


**Nota: no video eu pretendo mostras como ficou utilizando o menu q eu crie pois eu achei bem legal kkk**

ficando assim minhas imagens

![](../evidencias/Desafio/resultados/Desafio_resultados_14.png)