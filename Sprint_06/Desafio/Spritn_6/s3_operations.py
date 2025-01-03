import boto3
import logging
import os
from dotenv import load_dotenv
from datetime import datetime

# Carregar variáveis de ambiente
load_dotenv()

# Configuração de logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Configuração do cliente S3
s3 = boto3.client(
    's3',
    aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
    aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'),
    aws_session_token=os.getenv('AWS_SESSION_TOKEN')
)

def upload_file_s3(bucket_name, file_key, upload_path):
    """Faz o upload de um arquivo para o S3."""
    if not os.path.exists(upload_path):
        logging.error(f"Arquivo '{upload_path}' não encontrado. Upload cancelado.")
        return
    
    try:
        s3.upload_file(upload_path, bucket_name, file_key)
        logging.info(f"Arquivo '{file_key}' enviado com sucesso para o bucket '{bucket_name}'.")
    except Exception as e:
        logging.error(f"Erro ao enviar o arquivo: {e}")

if __name__ == "__main__":
    # Nome do bucket
    bucket_name = 'data-lake-do-thalles-lima'
    
    # Data do processamento
    data_atual = datetime.now()
    data_formatada = data_atual.strftime('%Y/%m/%d')
    
    # Configurar caminhos para os arquivos
    base_path = f"Raw/Local/CSV"
    movies_key = f"{base_path}/Movies/{data_formatada}/movies.csv"
    series_key = f"{base_path}/Series/{data_formatada}/series.csv"
    
   
upload_file_s3(bucket_name, movies_key, 'csv/movies.csv')
upload_file_s3(bucket_name, series_key, 'csv/series.csv')
 # Fazer upload dos arquivos para o bucket S3
#    upload_file_s3(bucket_name, movies_key, '../movies.csv')
 #   upload_file_s3(bucket_name, series_key, '../series.csv')
# Caminhos para os arquivos dentro do container