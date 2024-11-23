import sys
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from awsglue.utils import getResolvedOptions
from pyspark.sql.functions import col, upper, count, desc

# Obter parâmetros do Glue
args = getResolvedOptions(sys.argv, ["JOB_NAME"])

# Configurações do Glue
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args["JOB_NAME"], args)

# Caminhos no S3
input_path = "s3://aws-glue-assets-867344431452-us-east-1/lab-glue/input/nomes.csv"
output_path = "s3://aws-glue-assets-867344431452-us-east-1/lab-glue/frequencia_registro_nomes_eua/"

# 1. Ler o arquivo CSV no S3
df = spark.read.csv(input_path, header=True, inferSchema=True)

# 2. Imprimir o schema do DataFrame
print("Schema do DataFrame:")
df.printSchema()

# 3. Alterar os valores da coluna nome para MAIÚSCULO
df_upper = df.withColumn("nome", upper(col("nome")))

# 4. Imprimir a contagem de linhas presentes no DataFrame
print(f"Total de linhas no DataFrame: {df_upper.count()}")

# 5. Contar nomes agrupados por ano e sexo
df_grouped = df_upper.groupBy("ano", "sexo").agg(count("nome").alias("total_nomes"))
print("Contagem de nomes agrupados por ano e sexo:")
df_grouped.show()

# 6. Ordenar os dados pelo ano mais recente
df_sorted = df_upper.orderBy(col("ano").desc())
print("Dados ordenados pelo ano mais recente:")
df_sorted.show()

# 7. Nome feminino com mais registros e o ano
df_fem = df_upper.filter(col("sexo") == "F")
most_common_fem = df_fem.groupBy("ano", "nome").agg(count("*").alias("total")) \
    .orderBy(desc("total")).first()
print(f"Nome feminino mais registrado: {most_common_fem['nome']} em {most_common_fem['ano']}")

# 8. Nome masculino com mais registros e o ano
df_masc = df_upper.filter(col("sexo") == "M")
most_common_masc = df_masc.groupBy("ano", "nome").agg(count("*").alias("total")) \
    .orderBy(desc("total")).first()
print(f"Nome masculino mais registrado: {most_common_masc['nome']} em {most_common_masc['ano']}")

# 9. Total de registros masculinos e femininos para cada ano (primeiras 10 linhas)
df_year_totals = df_upper.groupBy("ano", "sexo").agg(count("*").alias("total")) \
    .orderBy("ano").limit(10)
print("Total de registros masculinos e femininos para os primeiros 10 anos:")
df_year_totals.show()

# 10. Escrever o DataFrame com nomes em maiúsculo no S3
df_upper.write.mode("overwrite").partitionBy("sexo", "ano").json(output_path)

# Finalizar o job
job.commit()
