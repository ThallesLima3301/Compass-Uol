import boto3
import logging
import os
from dotenv import load_dotenv

# Carregar variáveis de ambiente
load_dotenv()

# Configuração do cliente S3
s3 = boto3.client(
    's3',
    aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
    aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'),
    aws_session_token=os.getenv('AWS_SESSION_TOKEN')
)

def download_file_s3(bucket_name, file_key, download_path):
    """Faz o download de um arquivo do S3 para o caminho especificado."""
    try:
        s3.download_file(bucket_name, file_key, download_path)
        logging.info(f"Arquivo '{file_key}' baixado com sucesso do bucket '{bucket_name}'.")
    except Exception as e:
        logging.error(f"Erro ao baixar o arquivo: {e}")

def upload_file_s3(bucket_name, file_key, upload_path):
    """Faz o upload de um arquivo para o S3."""
    try:
        s3.upload_file(upload_path, bucket_name, file_key)
        logging.info(f"Arquivo '{file_key}' enviado com sucesso para o bucket '{bucket_name}'.")
    except Exception as e:
        logging.error(f"Erro ao enviar o arquivo: {e}")
