


Vou lá vou começar comentando sobre as dificuldades que enfrentei.

Tive que revisar e testar várias vezes a lógica de join entre os arquivos CSV e JSON.

Os regex utilizados para filtrar gêneros "comedy" e "animation" também foi complciado, pois precisei testar várias abordagens até encontrar case-insensitive.

Não  tive problemas com o meu modelo.



# DESAFIO


![alt text](../evidencias/Img_Desafio/image.png)


![alt text](../evidencias/Img_Desafio/image-1.png)

Comecei fazendo minha modelagem com base no que eu vou precisar para minha analise.

<h1>Analisar a Fonte dos Dados</h1>

CSV:

Tenho um arquivo CSV que possui as seguintes colunas:

id, titulopincipal, titulooriginal, anolancamento, tempominutos, genero, notamedia, numerovotos, generoartista, personagem, nomeartista, anonascimento, anofalecimento, profissao, titulosmaisconhecidos, partition_0.

JSON:

Meu JSON possui as seguintes colunas:
id, title, release_date, vote_average, vote_count, popularity, partition_0, partition_1, partition_2.


# Fiz usando DiagramaDB:

<h3>Passo a Passo para Modelagem do Star Schema no DiagramaDB</h3>

Identificação das Tabelas Fato e Dimensão

Com base nos arquivos CSV e JSON, identifiquei as principais entidades e métricas:

Tabela Fato: fato_comedia_animacao

Contém métricas como vote_average, vote_count e popularity, além de chaves estrangeiras para as dimensões.

Tabelas Dimensão:
dim_tempo: Data, ano e mês de lançamento.
dim_genero: Informações sobre o gênero.
dim_filme: Detalhes dos filmes, como títulos e ano de lançamento.
dim_artista: Informações dos artistas, como nome, gênero, profissão e anos de vida.

<h1>Estruturação da Tabela Fato</h1>

A tabela fato_comedia_animacao foi criada como a tabela central. Ela conecta todas as dimensões e contém as métricas necessárias.

id: Chave primária para cada registro.
tempo_id: Chave estrangeira para dim_tempo.
genero_id: Chave estrangeira para dim_genero.
filme_id: Chave estrangeira para dim_filme.
artista_id: Chave estrangeira para dim_artista.
vote_average, vote_count e popularity: Métricas numéricas.


# Criação das Tabelas Dimensão

<h1>dim_tempo</h1>

Armazena os dados relacionados ao tempo, extraídos do JSON (release_date).

id: Chave primária.
release_date: Data completa de lançamento.
ano: Ano de lançamento.
mes: Mês de lançamento.


<h1>dim_genero</h1>
Contém informações únicas sobre os gêneros dos filmes.

id: Chave primária.
genero: Nome do gênero (ex: Comédia, Animação).


<h1>dim_filme</h1>
Armazena detalhes específicos sobre os filmes, combinando dados do CSV e JSON.

id: Chave primária.
titulo_principal: Título principal.
titulo_original: Título original.
ano_lancamento: Ano de lançamento.
ano: Duração (em minutos) se necessário.
popularity: Indicador de popularidade.


<h1>dim_artista </h1>
Guarda informações detalhadas dos artistas presentes nos filmes.

id: Chave primária.
nomeartista: Nome do artista.
genero_artista: Gênero do artista.
profissao: Função do artista (ator, diretor, etc.).
anonascimento: Ano de nascimento.
anofalecimento: Ano de falecimento (se aplicável).

# Estrutura Final
<body>
    <table>
        <caption>3. Estrutura Final</caption>
        <thead>
            <tr>
                <th>Tabela</th>
                <th>Colunas Principais</th>
                <th>Descrição</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>Dim_Filme</td>
                <td>id, titulo_principal, titulo_original, ano_lancamento, ano, popularity</td>
                <td>Informações principais dos filmes ou séries.</td>
            </tr>
            <tr>
                <td>Dim_Artista</td>
                <td>id, nomeartista, genero_artista, anonascimento, anofalecimento, profissao</td>
                <td>Informações principais sobre os artistas.</td>
            </tr>
            <tr>
                <td>Dim_Tempo</td>
                <td>id, release_date, ano, mes</td>
                <td>Informações de tempo relacionadas ao lançamento.</td>
            </tr>
            <tr>
                <td>Dim_Genero</td>
                <td>id, genero</td>
                <td>Informações sobre os gêneros dos filmes ou séries.</td>
            </tr>
            <tr>
                <td>Fato_Comedia_Animacao</td>
                <td>id, tempo_id, genero_id, filme_id, artista_id, vote_average, vote_count, popularity, mse, mae</td>
                <td>Dados analíticos sobre avaliações, popularidade e métricas de erro.</td>
            </tr>
        </tbody>
    </table>
</body>


# Relacionamentos Entre Tabelas

As chaves estrangeiras conectam as tabelas dimensão à tabela fato:


tempo_id → dim_tempo.id

genero_id → dim_genero.id

filme_id → dim_filme.id

artista_id → dim_artista.id

Resultado:

![alt text](../evidencias/Img_Desafio/image_1.png)

Beleza, agora eu vou criar o passo a passo para minha camada refined

# Passo a Passo - Construção da Camada Refined

Importar Bibliotecas Necessárias
GlueContext, DynamicFrame, pyspark, functions, sys, getResolvedOptions.

Capturar Parâmetros de Entrada

Defino os parâmetros do Glue Job:

JOB_NAME: Nome do job.
INPUT_PATH_CSV e INPUT_PATH_JSON: Caminhos no S3 para os arquivos Trusted (CSV e JSON).
OUTPUT_BASE_PATH: Caminho no S3 para salvar as saídas Refined.



![alt text](../evidencias/Img_Desafio/image-3.png)

Leitura dos Dados Trusted
Carrego os dados do S3:
Formato Parquet para os dois arquivos (CSV e JSON).
Converto para DataFrame do Spark.



![alt text](../evidencias/Img_Desafio/image-2.png)

Renomear Colunas para Evitar Ambiguidade
Para evitar conflitos entre colunas do CSV e JSON, renomeio os campos que possuem o mesmo nome.


![alt text](../evidencias/Img_Desafio/image-4.png)

Filtrar Filmes Comuns Entre os Arquivos
Realizo o JOIN entre os dois DataFrames usando os títulos (titulopincipal e title) como chave. Renomeio o título para "titulo_principal" para consistência.


![alt text](../evidencias/Img_Desafio/image-5.png)

Resolver Valores Duplicados com Coalesce
Uso a função coalesce para priorizar os valores do CSV, caso existam duplicidades.



![alt text](../evidencias/Img_Desafio/image-6.png)


<h2>Dim_Tempo</h2>

Extraio a data, ano e mês do campo release_date.


![alt text](../evidencias/Img_Desafio/image-7.png)

<h2>Dim_Genero</h2>

Filtra gêneros que contenham "comedy" ou "animation".


![alt text](../evidencias/Img_Desafio/image-8.png)


<h2>Dim_Filme</h2>

Seleciono os atributos dos filmes e crio a dimensão.


![alt text](../evidencias/Img_Desafio/image-9.png)


<h2>Dim_Artista</h2>

Seleciono informações dos artistas.


![alt text](../evidencias/Img_Desafio/image-10.png)

<h2>Tabela Fato</h2>

Filtra apenas filmes de Comédia/Animação entre 2000 e 2020 e particiona por ano.


![alt text](../evidencias/Img_Desafio/image-11.png)


![alt text](../evidencias/Img_Desafio/image-12.png)

MSE AND MAE

Leitura e Preparação dos Dados

Primeiro, eu li os dados de arquivos CSV e JSON do S3 e os converti para DataFrames do Spark.

Eu renomeei algumas colunas nos dois DataFrames para evitar ambiguidade durante a união.

Filtragem e União dos Dados

Em seguida, eu fiz uma junção interna entre os DataFrames CSV e JSON.

A junção foi feita com base no título, tratando espaços e letras maiúsculas/minúsculas.

Eu também apliquei uma deduplicação para garantir que não houvesse registros duplicados.

Criação da Coluna vote_predicted

Para simular as previsões, eu criei a coluna vote_predicted.

A previsão foi feita adicionando uma variação aleatória de até 10% ao valor de vote_average.

Cálculo do MSE (Mean Squared Error)

Eu calculei o erro quadrático médio

ara isso, utilizei o PySpark para calcular a média dos quadrados das diferenças entre vote_average e vote_predicted.

`mse = fato_comedia_animacao.select(`
   `F.mean((F.col("vote_average") - F.col("vote_predicted")) 2).alias("MSE")`
`).first()["MSE"]`


![alt text](../evidencias/Img_Desafio/image-29.png)

Cálculo do MAE (Mean Absolute Error)

O erro absoluto médio 


Assim como no cálculo do MSE, utilizei o PySpark para calcular a média dos valores absolutos das diferenças.

Adição das Colunas mse e mae na Tabela Fato

Adicionei as métricas MSE e MAE como colunas constantes na tabela fato fato_comedia_animacao.

criei dois pequenos DataFrames contendo os valores calculados de MSE e MAE.

Eles foram salvos em pastas separadas.

<h2>Resultado Final </h2>
Dim_Tempo, Dim_Genero, Dim_Filme, e Dim_Artista foram criadas e armazenadas em formato Parquet.
A Tabela Fato foi particionada por ano e salva no formato Parquet.
Os dados Trusted foram processados e estruturados na camada Refined, prontos para análise.


Agora eu vou criar um Crawler.

![alt text](../evidencias/Img_Desafio/image-13.png)

rodei ele, e fui ver minhas tabelas.

![alt text](../evidencias/Img_Desafio/image-14.png)


Beleza tudo certo agora vamos no athena fazer alguns teste para ver se esta tudo certo.


Verificando duplicadas 

![alt text](../evidencias/Img_Desafio/image-15.png)

![alt text](../evidencias/Img_Desafio/image-16.png)

![alt text](../evidencias/Img_Desafio/image-17.png)

![alt text](../evidencias/Img_Desafio/image-18.png)

![alt text](../evidencias/Img_Desafio/image-19.png)



verificando nulos 

![alt text](../evidencias/Img_Desafio/image-20.png)

![alt text](../evidencias/Img_Desafio/image-21.png)

![alt text](../evidencias/Img_Desafio/image-22.png)

![alt text](../evidencias/Img_Desafio/image-23.png)

![alt text](../evidencias/Img_Desafio/image-24.png)

![alt text](../evidencias/Img_Desafio/image-25.png)

vendo total de filme da minha fato_comedia_animacao

![alt text](../evidencias/Img_Desafio/image-26.png)

agora vendo minha dim_filme

![alt text](../evidencias/Img_Desafio/image-27.png)


**Nota: minha fato esta somente com os filmes em comum do json, ja minha dim_filme esta com todos os filmes**

Ja aqui estou vendo se todos os meu generos possui comedia ou animação

![alt text](../evidencias/Img_Desafio/image-28.png)

Beleza parece que ta tudo certo.

Vou explicar minha analise

Análise: Filmes de Comédia/Animação (2000-2020)

Objetivo:
Explorar a evolução de filmes do gênero Comédia/Animação entre os anos 2000 e 2020. A análise busca entender as avaliações médias, popularidade e qualidade das produções ao longo do tempo, destacando fatores que influenciam a aceitação do público e oferecendo insights preditivos e diagnósticos.

Etapas Principais da Análise:

Média de Notas por Ano

Análise: Calcular e observar a média das avaliações de filmes ao longo dos anos para identificar tendências.
Visualização: Gráfico de linha destacando mudanças na qualidade percebida.
Pergunta: Como as avaliações de Comédia/Animação evoluíram entre 2000 e 2020?

Análise Preditiva

Análise: Previsão de notas futuras para o gênero com técnicas simples de Machine Learning.
Métricas: Avaliar precisão com MSE (Mean Squared Error) e MAE (Mean Absolute Error).
Visualização: Scatter plot mostrando relação entre previsões e valores reais, com cards para exibir métricas.
Objetivo: Identificar tendências futuras e validar o modelo preditivo.

Análise Diagnóstica

Análise: Identificar erros e outliers que impactam a precisão do modelo preditivo.
Visualização: Gráfico de distribuição dos erros residuais, diagnosticando pontos de falha.
Objetivo: Diagnosticar problemas e otimizar previsões.

Evolução Temporal de Popularidade e Qualidade

Análise: Estudar a quantidade de lançamentos e as avaliações médias ao longo dos anos.
Visualização: Gráficos de linha mostrando tanto o número de lançamentos quanto a evolução das notas.
Pergunta: Como a produção e popularidade de Comédia/Animação mudaram de 2000 a 2020?

Objetivo Final:
Entender a evolução e tendências no gênero Comédia/Animação, gerando insights que auxiliem na identificação de fatores que influenciam popularidade e qualidade, com suporte em análises quantitativas, preditivas e diagnósticas.


Visualizações Finais

Análises em gráficos claros e objetivos:

Gráfico de Linha: Evolução da média de notas ao longo dos anos.

Gráfico de Linha: Evolução da popularidade média.

Histograma/Scatter Plot: Distribuição das notas médias.

Scatter Plot: Relação entre popularidade e nota média.

Gráfico de Barras: Top 10 filmes mais bem avaliados.





