import requests
import pandas as pd
import os
from IPython.display import display
from dotenv import load_dotenv

# Carregar as variáveis de ambiente do arquivo .env
load_dotenv()

# Obter a chave da API do arquivo .env
api_key = os.getenv("API_KEY")

# Validar se a chave foi carregada corretamente
if not api_key:
    print("Erro: API_KEY não encontrada. Verifique o arquivo .env.")
    exit()

# URL para obter os filmes mais bem avaliados
url = f"https://api.themoviedb.org/3/movie/top_rated?api_key={api_key}&language=pt-BR"

# Fazer a requisição à API
response = requests.get(url)

# Exibir o código de status da resposta
print("Status Code:", response.status_code)

# Verificar se a requisição foi bem-sucedida
if response.status_code != 200:
    print(f"Erro na requisição: {response.status_code}")
    print("Resposta da API:", response.json())
    exit()

# Obter os dados da resposta JSON
data = response.json()

# Validar se a resposta contém a chave 'results'
if 'results' not in data:
    print("Erro: A chave 'results' não foi encontrada na resposta da API.")
    print("Resposta completa:", data)
    exit()

# Processar os dados dos filmes
filmes = []
for movie in data['results']:
    filme = {
        'Título': movie['title'],
        'Data de lançamento': movie['release_date'],
        'Visão geral': movie['overview'],
        'Votos': movie['vote_count'],
        'Média de votos': movie['vote_average']
    }
    filmes.append(filme)

# Criar um DataFrame com os dados
df = pd.DataFrame(filmes)

# Exibir o DataFrame
display(df)
