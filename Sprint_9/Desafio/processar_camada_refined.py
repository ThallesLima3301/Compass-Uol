import sys
from awsglue.context import GlueContext
from awsglue.dynamicframe import DynamicFrame
from awsglue.utils import getResolvedOptions
from awsglue.job import Job
from pyspark.context import SparkContext
from pyspark.sql import functions as F
from pyspark.sql.functions import lit, to_date, coalesce

# Lendo os parâmetros passados via Job Parameters
args = getResolvedOptions(
    sys.argv, ['JOB_NAME', 'INPUT_PATH_CSV', 'INPUT_PATH_JSON', 'OUTPUT_BASE_PATH']
)

input_path_csv = args['INPUT_PATH_CSV']
input_path_json = args['INPUT_PATH_JSON']
output_base_path = args['OUTPUT_BASE_PATH']

# Inicializar o Glue Context
sc = SparkContext()
glueContext = GlueContext(sc)

# Inicializar o Job
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Leitura dos arquivos Trusted
csv_df = glueContext.create_dynamic_frame.from_options(
    connection_type="s3",
    connection_options={"paths": [input_path_csv]},
    format="parquet"
).toDF()

json_df = glueContext.create_dynamic_frame.from_options(
    connection_type="s3",
    connection_options={"paths": [input_path_json]},
    format="parquet"
).toDF()

# Renomear colunas no CSV para evitar ambiguidade
csv_df = csv_df.withColumnRenamed("id", "csv_id") \
               .withColumnRenamed("notaMedia", "csv_vote_average") \
               .withColumnRenamed("numeroVotos", "csv_vote_count")

# Renomear colunas no JSON para evitar ambiguidade
json_df = json_df.withColumnRenamed("id", "json_id") \
                 .withColumnRenamed("vote_average", "json_vote_average") \
                 .withColumnRenamed("vote_count", "json_vote_count")

# Filtrar apenas os filmes em comum entre CSV e JSON usando 'titulopincipal' e 'title'
common_movies = csv_df.join(
    json_df,
    F.trim(F.upper(csv_df["titulopincipal"])) == F.trim(F.upper(json_df["title"])),
    "inner"
).withColumnRenamed("titulopincipal", "titulo_principal")  # Renomear para consistência

# Resolver as colunas de ambiguidade unificando os valores
common_movies = common_movies.withColumn(
    "vote_average",
    coalesce(F.col("csv_vote_average"), F.col("json_vote_average"))  # Prioriza valores do CSV se existirem
).withColumn(
    "vote_count",
    coalesce(F.col("csv_vote_count"), F.col("json_vote_count"))  # Prioriza valores do CSV se existirem
)

# Aplicar deduplicação para garantir que registros repetidos sejam removidos
common_movies = common_movies.dropDuplicates(["titulo_principal", "release_date"])  # Remove duplicatas com base nesses campos

# Criar Dimensão Tempo
dim_tempo = common_movies.withColumn("release_date", to_date(F.col("release_date"), "yyyy-MM-dd")) \
    .select("release_date").distinct() \
    .withColumn("ano", F.year(F.col("release_date"))) \
    .withColumn("mes", F.month(F.col("release_date"))) \
    .filter((F.col("ano") >= 2000) & (F.col("ano") <= 2020))

dim_tempo.write.mode("overwrite").parquet(f"{output_base_path}/dim_tempo")

# Criar Dimensão Género
dim_genero = csv_df.select("genero").distinct() \
    .filter(
        F.col("genero").rlike("(?i)(comedy|animation)")  # Regex para 'comedy' ou 'animation' (case-insensitive)
    )

dim_genero.write.mode("overwrite").parquet(f"{output_base_path}/dim_genero")

# Criar Dimensão Filme
dim_filme = common_movies.select(
    F.col("csv_id").alias("id"),
    F.col("titulo_principal"),
    F.col("titulooriginal").alias("titulo_original"),
    F.col("release_date"),
    F.col("popularity")
).distinct() \
    .withColumn("ano", F.year(to_date(F.col("release_date"), "yyyy-MM-dd"))) \
    .filter((F.col("ano") >= 2000) & (F.col("ano") <= 2020))

dim_filme.write.mode("overwrite").parquet(f"{output_base_path}/dim_filme")

# Criar Dimensão Artista
dim_artista = csv_df.select(
    "nomeartista", "profissao", "generoartista", "anonascimento", "anofalecimento"
).distinct()

dim_artista.write.mode("overwrite").parquet(f"{output_base_path}/dim_artista")

# Criar Tabela Fato (Filtrar apenas os anos e gêneros relevantes)
fato_comedia_animacao = common_movies.withColumn("release_date", to_date(F.col("release_date"), "yyyy-MM-dd")) \
    .select(
        F.col("titulo_principal"),
        "vote_average",
        "vote_count",
        "popularity",
        "genero",
        "release_date"
    ) \
    .withColumn("ano", F.year(F.col("release_date"))) \
    .filter((F.col("ano") >= 2000) & (F.col("ano") <= 2020)) \
    .filter(
        F.col("genero").rlike("(?i)(comedy|animation)")  # Regex para filtrar gêneros
    )

# Criar a pasta principal 'fato_comedia_animacao' e particionar por ano
anos_distintos = fato_comedia_animacao.select("ano").distinct().collect()

for ano in anos_distintos:
    ano_valor = ano["ano"]
    fato_comedia_animacao.filter(F.col("ano") == ano_valor) \
        .write.mode("overwrite") \
        .parquet(f"{output_base_path}/fato_comedia_animacao/{ano_valor}")

# Finalizar o job
job.commit()
