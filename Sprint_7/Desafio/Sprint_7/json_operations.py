import requests
import json
import time
import os
import logging
from dotenv import load_dotenv

# Carregar variáveis de ambiente
load_dotenv()

# Configuração de logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger()

# Configurações de API e autenticação
API_KEY = os.getenv("API_KEY")
BASE_URL = "https://api.themoviedb.org/3"
HEADERS = {
    "accept": "application/json",
    "Authorization": f"Bearer {API_KEY}"
}

# Função para buscar filmes de um gênero específico por ano
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

# Função para obter detalhes de um filme específico
def fetch_movie_details(movie_id):
    url = f"{BASE_URL}/movie/{movie_id}"
    try:
        response = requests.get(url, headers=HEADERS)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        logger.error(f"Erro ao buscar detalhes do filme ID {movie_id}: {e}")
        return None

# Parâmetros de análise
GENRE_IDS = [35, 16]  # IDs de Comédia e Animação
anos = range(2000, 2020)  # Anos para análise

# Diretório para salvar os arquivos JSON
# Diretório para salvar os arquivos JSON
folder_path = 'json_files'
if not os.path.exists(folder_path):
    os.makedirs(folder_path)

# Limite de registros por arquivo JSON
MAX_RECORDS = 100
total_size_mb = 0  # Variável para acumular o tamanho total dos arquivos

# Loop para buscar dados de cada ano
for year in anos:
    all_movie_data = []  # Lista para armazenar dados temporariamente
    page = 1
    file_counter = 1  # Contador para nomear os arquivos

    while True:
        # Obter lista de filmes por ano e gênero
        movies = fetch_movies_by_year_and_genre(year, GENRE_IDS, page=page)
        if not movies or "results" not in movies:
            break

        # Extrair informações relevantes de cada filme
        for movie in movies["results"]:
            movie_id = movie["id"]
            title = movie.get("title", "N/A")
            release_date = movie.get("release_date", "N/A")
            vote_average = movie.get("vote_average", None)
            vote_count = movie.get("vote_count", None)
            popularity = movie.get("popularity", None)
            
            # Coletar dados detalhados se necessário
            movie_details = fetch_movie_details(movie_id)
            if movie_details:
                data = {
                    "id": movie_id,
                    "title": title,
                    "release_date": release_date,
                    "vote_average": vote_average,
                    "vote_count": vote_count,
                    "popularity": popularity
                }
                all_movie_data.append(data)

            # Salvar e limpar o buffer quando atingir o máximo de registros
            if len(all_movie_data) >= MAX_RECORDS:
                file_path = os.path.join(folder_path, f"{year}_comedy_animation_movies_part_{file_counter}.json")
                with open(file_path, "w") as f:
                    json.dump(all_movie_data, f, indent=4)
                
                # Obter o tamanho do arquivo JSON e acumular no total
                file_size = os.path.getsize(file_path) / (1024 * 1024)
                total_size_mb += file_size
                logger.info(f"Tamanho do arquivo '{file_path}': {file_size:.2f} MB")
                logger.info(f"Arquivo '{file_path}' salvo com {len(all_movie_data)} registros.")

                # Limpar os dados e incrementar o contador de arquivos
                all_movie_data = []
                file_counter += 1

        # Verificar se há mais páginas
        if page >= movies["total_pages"]:
            break
        else:
            page += 1
            time.sleep(0.1)  # Pausa para evitar limite de requisição

    # Salvar os registros restantes, se houver
    if all_movie_data:
        file_path = os.path.join(folder_path, f"{year}_comedy_animation_movies_part_{file_counter}.json")
        with open(file_path, "w") as f:
            json.dump(all_movie_data, f, indent=4)
        
        # Obter o tamanho do arquivo JSON e acumular no total
        file_size = os.path.getsize(file_path) / (1024 * 1024)
        total_size_mb += file_size
        logger.info(f"Tamanho do arquivo '{file_path}': {file_size:.2f} MB")
        logger.info(f"Arquivo '{file_path}' salvo com {len(all_movie_data)} registros.")

# Exibir o tamanho total de todos os arquivos
logger.info(f"Tamanho total de todos os arquivos JSON: {total_size_mb:.2f} MB")
logger.info("Coleta de dados concluída.")
