import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from awsglue.dynamicframe import DynamicFrame
from pyspark.sql.functions import when, col, lower, trim

# Definir os argumentos do Glue Job
args = getResolvedOptions(sys.argv, ['JOB_NAME', 'INPUT_PATH', 'OUTPUT_PATH'])

# Inicializar Glue
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# caminhos de entrada e saída
source_file = args['INPUT_PATH']
output_path = args['OUTPUT_PATH']

# Ler CSV como DynamicFrame
df = glueContext.create_dynamic_frame.from_options(
    connection_type="s3",
    connection_options={"paths": [source_file]},
    format="csv",
    format_options={
        "withHeader": True,
        "separator": "|"
    }
)

#  DynamicFrame para DataFrame para transformações
raw_data = df.toDF()

# Substituir valores "\\N" por null
df_no_nulls = raw_data.select(
    [when(col(c) == "\\N", None).otherwise(col(c)).alias(c) for c in raw_data.columns]
)

# Normalização das colunas de texto: converter para minúsculas e remover espaços extras
df_normalized = df_no_nulls
for col_name in df_normalized.columns:
    if dict(df_normalized.dtypes)[col_name] == "string":
        df_normalized = df_normalized.withColumn(col_name, trim(lower(col(col_name))))

# remover duplicatas
df_cleaned = df_normalized.dropDuplicates()

# remover linhas com valores nulos
df_cleaned = df_cleaned.na.drop()

# Converter de volta para DynamicFrame
clean_data = DynamicFrame.fromDF(df_cleaned, glueContext, "clean_data")

# Salvar os dados limpos no formato Parquet
glueContext.write_dynamic_frame.from_options(
    frame=clean_data,
    connection_type="s3",
    connection_options={"path": output_path},
    format="parquet"
)

# Finalizar o Job
job.commit()
