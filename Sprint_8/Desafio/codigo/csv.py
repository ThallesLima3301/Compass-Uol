import sys
from datetime import datetime
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from awsglue.dynamicframe import DynamicFrame
from pyspark.sql.functions import when, col, lower, trim

# Receber o nome do job e os caminhos S3
args = getResolvedOptions(sys.argv, ['JOB_NAME', 'INPUT_PATH', 'OUTPUT_BASE_PATH'])

# Inicializar o Glue Context
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Caminhos de entrada e saída
source_file = args['INPUT_PATH']
output_path = args['OUTPUT_BASE_PATH']

# Ler o arquivo CSV como DynamicFrame
df = glueContext.create_dynamic_frame.from_options(
    connection_type="s3",
    connection_options={"paths": [source_file]},
    format="csv",
    format_options={"withHeader": True, "separator": "|"}
)

# Converter o DynamicFrame para DataFrame para transformações
raw_data = df.toDF()

# Substituir zeros por null em todas as colunas
df_no_zeros = raw_data.select(
    [when(col(c) == 0, None).otherwise(col(c)).alias(c) for c in raw_data.columns]
)

# Normalização das colunas de texto: converter para minúsculas e remover espaços extras
for col_name in df_no_zeros.columns:
    if dict(df_no_zeros.dtypes)[col_name] == 'string':
        df_no_zeros = df_no_zeros.withColumn(col_name, trim(lower(col(col_name))))

# Remover duplicatas
df_cleaned = df_no_zeros.dropDuplicates()

# Remover colunas de particionamento indesejadas
columns_to_remove = ['partition_0', 'partition_1', 'partition_2', 'partition_3']
df_cleaned = df_cleaned.drop(*columns_to_remove)

# Remover linhas com valores nulos (se necessário)
df_cleaned = df_cleaned.na.drop()

# Converter de volta para DynamicFrame
clean_data = DynamicFrame.fromDF(df_cleaned, glueContext, "clean_data")

# Salvar os dados limpos no formato Parquet no caminho direto do OUTPUT_PATH
glueContext.write_dynamic_frame.from_options(
    frame=clean_data,
    connection_type="s3",
    connection_options={"path": output_path},
    format="parquet"
)

# Finalizar o Job
job.commit()
