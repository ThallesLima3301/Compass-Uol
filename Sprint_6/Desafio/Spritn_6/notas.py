# notamaxima.py

from utils import load_data

def main():
    # Caminhos para os arquivos
    movies_path = 'csv/movies.csv'
    series_path = 'csv/series.csv'
    
    # Carregar dados
    movies_df = load_data(movies_path)
    series_df = load_data(series_path)
    
    # Contar produções com nota máxima (10) para todos os filmes e séries
    movies_max_count = movies_df[movies_df['notaMedia'] == 10].shape[0]
    series_max_count = series_df[series_df['notaMedia'] == 10].shape[0]
    print("Total de Filmes com nota máxima:", movies_max_count)
    print("Total de Séries com nota máxima:", series_max_count)

    # Filtrar séries de Animação com nota máxima (nota 10) PARA TESTE
    #animation_series_max = series_df[(series_df['genero'].str.contains('Animation', case=False, na=False)) & (series_df['notaMedia'] == 10)]
    #top_13_animation_series_max = animation_series_max.head(13)
    
    # Contar filmes e séries de Comédia e Animação com nota máxima (10)
    
    comedy_movies_max_count = movies_df[(movies_df['genero'].str.contains('Comedy', case=False, na=False)) & (movies_df['notaMedia'] == 10)].shape[0]
    animation_movies_max_count = movies_df[(movies_df['genero'].str.contains('Animation', case=False, na=False)) & (movies_df['notaMedia'] == 10)].shape[0]
    comedy_series_max_count = series_df[(series_df['genero'].str.contains('Comedy', case=False, na=False)) & (series_df['notaMedia'] == 10)].shape[0]
    animation_series_max_count = series_df[(series_df['genero'].str.contains('Animation', case=False, na=False)) & (series_df['notaMedia'] == 10)].shape[0]
    
    # Exibir as contagens específicas para Comédia e Animação
    print("\nFilmes de Comédia com nota máxima:", comedy_movies_max_count)
    print("Filmes de Animação com nota máxima:", animation_movies_max_count)
    print("Séries de Comédia com nota máxima:", comedy_series_max_count)
    print("Séries de Animação com nota máxima:", animation_series_max_count)
   
    # Exibir as séries filtradas
    #print("As 13 Séries de Animação com Nota Máxima:")
    #print(top_13_animation_series_max[['tituloPincipal', 'anoLancamento', 'notaMedia']])

    
    # Calcular a média de notas para Comédia e Animação
    comedy_movies_avg = movies_df[movies_df['genero'].str.contains('Comedy', case=False, na=False)]['notaMedia'].mean()
    animation_movies_avg = movies_df[movies_df['genero'].str.contains('Animation', case=False, na=False)]['notaMedia'].mean()
    comedy_series_avg = series_df[series_df['genero'].str.contains('Comedy', case=False, na=False)]['notaMedia'].mean()
    animation_series_avg = series_df[series_df['genero'].str.contains('Animation', case=False, na=False)]['notaMedia'].mean()
    
    # Exibir as médias
    print("\nMédia de notas para filmes de Comédia:", comedy_movies_avg)
    print("Média de notas para filmes de Animação:", animation_movies_avg)
    print("Média de notas para séries de Comédia:", comedy_series_avg)
    print("Média de notas para séries de Animação:", animation_series_avg)

if __name__ == "__main__":
    main()
