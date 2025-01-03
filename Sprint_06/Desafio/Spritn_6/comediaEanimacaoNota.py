import pandas as pd
from utils import load_data, plot_top_genre_ratings

def main():
    # Caminhos para os arquivos
    movies_path = 'csv/movies.csv'
    series_path = 'csv/series.csv'
    
    # Carregar dados de filmes e séries
    movies_df = load_data(movies_path)
    series_df = load_data(series_path)
    
    # Filtrar para o tema Animation e Comedy com nota máxima
    animation_movies_10 = movies_df[(movies_df['genero'].str.contains('Animation', case=False, na=False)) & (movies_df['notaMedia'] == 10)]
    comedy_movies_10 = movies_df[(movies_df['genero'].str.contains('Comedy', case=False, na=False)) & (movies_df['notaMedia'] == 10)]
    animation_series_10 = series_df[(series_df['genero'].str.contains('Animation', case=False, na=False)) & (series_df['notaMedia'] == 10)]
    comedy_series_10 = series_df[(series_df['genero'].str.contains('Comedy', case=False, na=False)) & (series_df['notaMedia'] == 10)]
    
    # Exibir Top 10 Filmes e Séries de Animação com Nota Máxima
    print("Top 10 Filmes de Animação com Nota 10:")
    print(animation_movies_10[['tituloPincipal', 'anoLancamento', 'notaMedia']].drop_duplicates().head(10))
    
    print("\nTop 10 Séries de Animação com Nota 10:")
    print(animation_series_10[['tituloPincipal', 'anoLancamento', 'notaMedia']].drop_duplicates().head(10))
    
    # Exibir Top 10 Filmes e Séries de Comédia com Nota Máxima
    print("\nTop 10 Filmes de Comédia com Nota 10:")
    print(comedy_movies_10[['tituloPincipal', 'anoLancamento', 'notaMedia']].drop_duplicates().head(10))
    
    print("\nTop 10 Séries de Comédia com Nota 10:")
    print(comedy_series_10[['tituloPincipal', 'anoLancamento', 'notaMedia']].drop_duplicates().head(10))

    # Gerar gráficos para top 10 Animation e Comedy para filmes e séries com foco em nota média
    plot_top_genre_ratings(animation_movies_10, 'Filmes de Animação com Nota Máxima')
    plot_top_genre_ratings(comedy_movies_10, 'Filmes de Comédia com Nota Máxima')
    plot_top_genre_ratings(animation_series_10, 'Séries de Animação com Nota Máxima')
    plot_top_genre_ratings(comedy_series_10, 'Séries de Comédia com Nota Máxima')

if __name__ == "__main__":
    main()
