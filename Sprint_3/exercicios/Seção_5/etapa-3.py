"""
Resumo do que  fazer:
Ler a coluna "Average per Movie" (provavelmente é a quarta coluna, índice 3).
Encontrar o valor mais alto nessa coluna.
Exibir o nome do ator/atriz com a maior média.

Como é calculada a média "Average per Movie":
Somar o total de receita bruta do ator: Isso está na coluna "Total Gross" (segunda coluna), que representa a receita total de todos os filmes em que o ator participou.
Dividir pelo número de filmes: O número de filmes em que o ator participou está na coluna "Number of Movies" (terceira coluna).

                         Total Gross
Average per Movie = ---------------------
                     Number of Movies

Plano:
Ler o arquivo CSV.
Ignorar o cabeçalho.
Verificar a coluna "Average per Movie" para cada linha e comparar os valores.
Armazenar o nome do ator/atriz com o maior valor dessa coluna.
Exibir o nome e o valor correspondente.
"""

file_path = '../actors.csv'

try:
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Variáveis para armazenar o ator/atriz com maior média de receita por filme
    maior_media = 0
    ator_com_maior_media = ''

    # Processar cada linha a partir da segunda (ignorando o cabeçalho)
    for line in lines[1:]:
        dados = line.split(',')
        try:
            # Coluna 'Average per Movie' está na posição 3
            media_per_movie = float(dados[3].strip())
            ator = dados[0].strip()

            # Verificar se esta é a maior média encontrada
            if media_per_movie > maior_media:
                maior_media = media_per_movie
                ator_com_maior_media = ator

        except ValueError:
            # Se houver um erro de conversão, ignorar essa linha e continuar
            continue

    # Exibir o resultado
    if ator_com_maior_media:
        print(f"O ator/atriz com a maior media de receita por filme e {ator_com_maior_media}, com {maior_media:.2f} milhoes de dolares por filme.")
    else:
        print("Nenhuma média válida encontrada.")

except FileNotFoundError:
    print(f"Arquivo '{file_path}' nao encontrado.")
