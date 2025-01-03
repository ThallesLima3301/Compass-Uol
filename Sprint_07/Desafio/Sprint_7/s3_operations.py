import boto3
import logging
import os
from dotenv import load_dotenv
from datetime import datetime

# carregar variáveis de ambiente
load_dotenv()

# configuração de logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger()

# configuração do cliente S3
s3 = boto3.client(
    's3',
    aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
    aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'),
    aws_session_token=os.getenv('AWS_SESSION_TOKEN')  
)

def upload_file_s3(bucket_name, file_key, upload_path):
    """Faz o upload de um arquivo para o S3."""
    if not os.path.exists(upload_path):
        logger.error(f"Arquivo '{upload_path}' não encontrado. Upload cancelado.")
        return
    
    try:
        s3.upload_file(upload_path, bucket_name, file_key)
        logger.info(f"Arquivo '{file_key}' enviado com sucesso para o bucket '{bucket_name}'.")
    except Exception as e:
        logger.error(f"Erro ao enviar o arquivo: {e}")

def generate_file_keys(base_path, year, file_name):
    """Gera o caminho completo para o arquivo no S3 no formato desejado."""
    data_atual = datetime.now()
    data_formatada = data_atual.strftime('%Y/%m/%d')
    
    return f"{base_path}/TMDB/JSON/{data_formatada}/{year}_{file_name}"

def upload_all_files_in_directory(directory_path, bucket_name, base_path):
    """Envia todos os arquivos JSON da pasta especificada para o S3."""
    for file_name in os.listdir(directory_path):
        if file_name.endswith(".json"):
            year = file_name.split("_")[0]  # Extrai o ano do nome do arquivo
            file_path = os.path.join(directory_path, file_name)
            file_key = generate_file_keys(base_path, year, file_name)
            upload_file_s3(bucket_name, file_key, file_path)

if __name__ == "__main__":
    # nome do bucket (carregado do .env)
    bucket_name = os.getenv("S3_BUCKET_NAME")
    
    # caminho base para os arquivos no S3
    base_path = "Raw"
    
    # Pasta local contendo os arquivos JSON
    directory_path = 'json_files'

    # Fazer upload de todos os arquivos JSON na pasta especificada
    upload_all_files_in_directory(directory_path, bucket_name, base_path)
