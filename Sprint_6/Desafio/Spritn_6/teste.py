import pandas as pd

# Caminhos para os arquivos
movies_path = 'csv/movies.csv'
series_path = 'csv/series.csv'


# Lendo cada arquivo com o delimitador "|"
movies_df = pd.read_csv(movies_path, delimiter='|', low_memory=False)
series_df = pd.read_csv(series_path, delimiter='|', low_memory=False)

# Exibindo as primeiras linhas de cada arquivo para verificar

# Exibe a linha de cabeçalho com o nome das colunas
print(" | ".join(movies_df.columns))

print("Movies DataFrame:")
print(movies_df.head())



print(" | ".join(series_df.columns))

print("\nSeries DataFrame:")
print(series_df.head())

# Concatenando filmes e séries para análise conjunta
all_genres = pd.concat([movies_df['genero'], series_df['genero']])

# Separando os gêneros individuais
unique_genres = set()
for genres in all_genres.dropna():
    individual_genres = genres.split(',')
    unique_genres.update(individual_genres)

# Exibindo os gêneros únicos
print("Gêneros individuais presentes nos arquivos:")
for genre in sorted(unique_genres):
    print(genre.strip())