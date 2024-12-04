# -*- coding: utf-8 -*-
"""Apache_Spark.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1l9Wb6TGb9EfwBbdoojyYDA0j88JVOt6f
"""

!pip install pyspark

from google.colab import drive
drive.mount('/content/drive')

# Importando as bibliotecas necessárias
from pyspark.sql import SparkSession

# Criando a SparkSession
spark = SparkSession.builder \
    .master("local[*]") \
    .appName("Exercicio Spark") \
    .getOrCreate()

# Lendo o arquivo do Google Drive
caminho_arquivo = ("/content/drive/MyDrive/Colab Notebooks/nomes_aleatorios.txt")
df_nomes = spark.read.text(caminho_arquivo)

# Exibindo as primeiras 10 linhas do DataFrame
df_nomes.show(10)

# Renomeando a coluna para "Nome"
df_nomes = df_nomes.withColumnRenamed("_c0", "Nome")

# Exibindo o esquema do DataFrame
df_nomes.printSchema()

# Exibindo as primeiras 10 linhas do DataFrame
df_nomes.show(10)

from pyspark.sql.functions import lit, when, rand

# Adicionando a coluna "Escolaridade" com valores aleatórios
df_nomes = df_nomes.withColumn(
    "Escolaridade",
    when(rand() < 0.33, "Fundamental").when(rand() < 0.66, "Médio").otherwise("Superior")
)

# Exibindo as primeiras 10 linhas com a nova coluna
df_nomes.show(10)

from pyspark.sql.functions import col

# Lista de países da América do Sul
paises = ["Brasil", "Argentina", "Chile", "Peru", "Colômbia", "Uruguai",
          "Paraguai", "Equador", "Venezuela", "Bolívia", "Suriname",
          "Guiana", "Guiana Francesa"]

# Adicionando a coluna "País" com valores aleatórios da lista de países
df_nomes = df_nomes.withColumn(
    "País",
    when((rand() * len(paises)).cast("int") == 0, "Brasil")
    .when((rand() * len(paises)).cast("int") == 1, "Argentina")
    .when((rand() * len(paises)).cast("int") == 2, "Chile")
    .when((rand() * len(paises)).cast("int") == 3, "Peru")
    .when((rand() * len(paises)).cast("int") == 4, "Colômbia")
    .when((rand() * len(paises)).cast("int") == 5, "Uruguai")
    .when((rand() * len(paises)).cast("int") == 6, "Paraguai")
    .when((rand() * len(paises)).cast("int") == 7, "Equador")
    .when((rand() * len(paises)).cast("int") == 8, "Venezuela")
    .when((rand() * len(paises)).cast("int") == 9, "Bolívia")
    .when((rand() * len(paises)).cast("int") == 10, "Suriname")
    .when((rand() * len(paises)).cast("int") == 11, "Guiana")
    .otherwise("Guiana Francesa")
)

# Exibindo as primeiras 10 linhas com a nova coluna
df_nomes.show(10)

from pyspark.sql.functions import expr

# Adicionando a coluna "AnoNascimento" com valores aleatórios entre 1945 e 2010
df_nomes = df_nomes.withColumn(
    "AnoNascimento",
    (rand() * (2010 - 1945) + 1945).cast("int")  # Gera valores aleatórios e converte para inteiro
)

# Exibindo as primeiras 10 linhas com a nova coluna
df_nomes.show(10)

# Filtrando pessoas nascidas neste século (a partir de 2000)
df_seculo = df_nomes.filter(df_nomes["AnoNascimento"] >= 2000)

# Exibindo as primeiras 10 linhas do novo DataFrame
df_seculo.show(10)

# Criando uma tabela temporária chamada "pessoas"
df_nomes.createOrReplaceTempView("pessoas")

# Executando a consulta SQL para filtrar pessoas nascidas neste século
df_seculo_sql = spark.sql("SELECT * FROM pessoas WHERE AnoNascimento >= 2000")

# Exibindo as primeiras 10 linhas do resultado
df_seculo_sql.show(10)

# Filtrando pessoas da geração Millennials (1980 a 1994)
df_millennials = df_nomes.filter((df_nomes["AnoNascimento"] >= 1980) & (df_nomes["AnoNascimento"] <= 1994))

# Contando o número de pessoas
num_millennials = df_millennials.count()

# Exibindo o resultado
print(f"Número de pessoas da geração Millennials: {num_millennials}")

# Consulta SQL para contar as pessoas da geração Millennials
query_millennials = """
    SELECT COUNT(*) as num_millennials
    FROM pessoas
    WHERE AnoNascimento >= 1980 AND AnoNascimento <= 1994
"""

# Executando a consulta SQL
resultado_millennials = spark.sql(query_millennials)

# Exibindo o resultado
resultado_millennials.show()

query_geracoes = """
    SELECT
        `País` AS Pais,
        CASE
            WHEN AnoNascimento >= 1944 AND AnoNascimento <= 1964 THEN 'Baby Boomers'
            WHEN AnoNascimento >= 1965 AND AnoNascimento <= 1979 THEN 'Geracao X'
            WHEN AnoNascimento >= 1980 AND AnoNascimento <= 1994 THEN 'Millennials'
            WHEN AnoNascimento >= 1995 AND AnoNascimento <= 2015 THEN 'Geracao Z'
        END AS Geracao,
        COUNT(*) as Quantidade
    FROM pessoas
    GROUP BY `País`, Geracao
    ORDER BY `País`, Geracao
"""

# Executando a consulta SQL
resultado_geracoes = spark.sql(query_geracoes)

# Exibindo o resultado
resultado_geracoes.show(50, truncate=False)