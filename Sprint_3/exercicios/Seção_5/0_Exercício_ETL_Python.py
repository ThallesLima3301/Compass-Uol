""" O arquivo actors.csv tem a seguinte estrutura com as colunas:

Actor: Nome do ator/atriz.
Total Gross: Receita bruta de bilheteria doméstica, em milhões de dólares.
Number of Movies: Número de filmes em que o ator participou.
Average per Movie: Receita bruta dividida pelo número de filmes.
#1 Movie: Filme de maior receita bruta em que o ator participou.
Gross: Receita bruta, em milhões de dólares, do filme de maior receita.
Vamos começar pela Etapa 1: Encontrar o ator/atriz com o maior número de filmes.
"""

# Definir o caminho do arquivo corretamente
# Optei por utilizar um bloco try porque percebi que estava cometendo alguns erros durante o processo.
file_path = '../actors.csv'
try:
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Mostrar as primeiras 5 linhas para verificar o conteúdo
    print("Arquivo lido com sucesso. As primeiras 5 linhas sao:")
    for line in lines[:5]:
        print(line.strip())
except FileNotFoundError:
    print(f"Arquivo '{file_path}' nao encontrado. Verifique o caminho.")


