import sys
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.dynamicframe import DynamicFrame
from datetime import datetime
from pyspark.sql.functions import lit
from pyspark.sql import SparkSession

# Inicialização do Glue Context
glueContext = GlueContext(SparkContext.getOrCreate())
spark = glueContext.spark_session

# Lendo os parâmetros passados via Job Parameters
args = sys.argv
input_path = args[args.index("--INPUT_PATH") + 1] # testei esse + 1 pra ver a diferença
output_base_path = args[args.index("--OUTPUT_BASE_PATH") + 1]

# obter a data atual para construir o caminho dinâmico
current_date = datetime.now()
year_value = current_date.year
month_value = f"{current_date.month:02d}"  # Formato 2 dígitos exemplo 09/12/2024
day_value = f"{current_date.day:02d}"

# caminho de saída
output_path = f"{output_base_path}{year_value}/{month_value}/{day_value}/"

# Leitura dos dados JSON da Raw Zone
dyf_raw = glueContext.create_dynamic_frame.from_options(
    connection_type="s3",
    connection_options={"paths": [input_path]},
    format="json"
)

# Conversão para DataFrame
df = dyf_raw.toDF()

# Limpeza de dados
# remover duplicatas com base em colunas-chave
df_cleaned = df.dropDuplicates(["id", "title"])

# Remover valores nulos
df_cleaned = df_cleaned.na.drop()

# Conversão para DynamicFrame
dyf_cleaned = DynamicFrame.fromDF(df_cleaned, glueContext, "dyf_cleaned")

# Escrita no formato PARQUET diretamente no S3 com caminho dinâmico
glueContext.write_dynamic_frame.from_options(
    frame=dyf_cleaned,
    connection_type="s3",
    connection_options={"path": output_path},
    format="parquet"
)
