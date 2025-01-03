import os
import json
import requests
import logging
from dotenv import load_dotenv
import boto3
from datetime import datetime

# Carregar variáveis de ambiente
load_dotenv()

# configuração de logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger()

# configurações de API e autenticação
API_KEY = os.getenv("API_KEY")
S3_BUCKET_NAME = os.getenv("S3_BUCKET_NAME")

BASE_URL = "https://api.themoviedb.org/3"

HEADERS = {
    "accept": "application/json",
    "Authorization": f"Bearer {API_KEY}"
}

# Funçao para buscar filmes de um genero específico por ano
def fetch_movies_by_year_and_genre(year, genre_ids, page=1):
    url = f"{BASE_URL}/discover/movie"
    params = {
        "primary_release_year": year,
        "with_genres": ",".join(map(str, genre_ids)),
        "language": "en-US",
        "sort_by": "popularity.desc",
        "page": page
    }
    try:
        response = requests.get(url, headers=HEADERS, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        logger.error(f"Erro ao buscar filmes: {e}")
        return None

def generate_file_keys(base_path, year):
    """Gera o caminho completo para o arquivo no S3 com base no ano e data atual."""
    # Obter a data atual
    current_date = datetime.now()
    data_formatada = current_date.strftime('%Y/%m/%d')  # Formato ano/mês/dia

    # gerar o caminho final para o arquivo JSON
    return f"{base_path}/TMDB/JSON/{data_formatada}/{year}_comedy_animation_movies.json"

def lambda_handler(event, context):
    GENRE_IDS = [35, 16]  # IDs de comédia e animação usei um codigo a parte para pegar todos os IDs do TMDB
    anos = range(2000, 2021)  # Anos para análise

    # Caminho base para os arquivos no S3
    base_path = "Raw"  # Exemplo de caminho base

    # Loop para buscar dados de cada ano
    for year in anos:
        all_movie_data = []  # Lista para armazenar os dados de cada ano
        page = 1
        while True:
            movies = fetch_movies_by_year_and_genre(year, GENRE_IDS, page=page)
            if not movies or "results" not in movies:
                break

            for movie in movies["results"]:
                movie_data = {
                    "id": movie["id"],
                    "title": movie.get("title", "N/A"),
                    "release_date": movie.get("release_date", "N/A"),
                    "vote_average": movie.get("vote_average", None),
                    "vote_count": movie.get("vote_count", None),
                    "popularity": movie.get("popularity", None)
                }
                all_movie_data.append(movie_data)

            if page >= movies["total_pages"]:
                break
            else:
                page += 1

        # Gerar a chave do arquivo no S3 usando a função generate_file_keys
        s3_key = generate_file_keys(base_path, year)

        # Enviar os dados coletados para o S3
        s3 = boto3.client('s3')
        s3.put_object(Bucket=S3_BUCKET_NAME, Key=s3_key, Body=json.dumps(all_movie_data, indent=4))

        logger.info(f"Arquivo {s3_key} enviado para o S3 com sucesso.")

    return {
        'statusCode': 200,
        'body': json.dumps('Processamento concluído com sucesso!')
    }

# Teste local
if __name__ == "__main__":
    lambda_handler(None, None)
