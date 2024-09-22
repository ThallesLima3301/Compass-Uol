"""
Na Etapa 4, precisamos realizar a contagem de quantas vezes cada filme, contido na coluna "#1 Movie", aparece no dataset. Além disso, devo listar os filmes em ordem decrescente de quantidade de aparições, e, em caso de empate, ordenar alfabeticamente pelo nome do filme.

A saída deve seguir o formato:



Plano:
Ler o arquivo CSV e extrair a coluna "#1 Movie".
Contar quantas vezes cada filme aparece.
Ordenar os filmes de acordo com a quantidade (em ordem decrescente).
Se houver empate no número de aparições, ordenar os filmes alfabeticamente.
Escrever os resultados no formato solicitado.
"""

print('Sem usar  o from collections import Counter')

file_path = '../actors.csv'

try:
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # direcionamento  para armazenar os filmes e suas quantidades
    contagem_filmes = {}

    # processando cada linha a partir da segunda (ignorando o cabeçalho)
    for line in lines[1:]:
        dados = line.split(',')
        filme = dados[4].strip()  # coluna '#1 Movie' (posicao 4)

        # Se o filme já está no dicionário, incrementamos sua contagem
        if filme in contagem_filmes:
            contagem_filmes[filme] += 1
        else:
            # Caso contrário, adicionamos o filme com contagem inicial de 1
            contagem_filmes[filme] = 1

    # Ordenar os filmes pela quantidade (decrescente) e pelo nome em ordem alfabética
    filmes_ordenados = sorted(contagem_filmes.items(), key=lambda x: (-x[1], x[0]))

    # Exibir a saída no formato solicitado
    for idx, (filme, quantidade) in enumerate(filmes_ordenados, start=1):
        print(f"{idx} - O filme {filme} aparece {quantidade} vez(es) no dataset.")

except FileNotFoundError:
    print(f"Arquivo '{file_path}' nao encontrado.")

print('')
print('')
print('Utilizando o from collections import Counter')

from collections import Counter

file_path = '../actors.csv'

try:
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Variável para armazenar todos os filmes da coluna '#1 Movie'
    filmes = []

    # Processar cada linha a partir da segunda (ignorando o cabeçalho)
    for line in lines[1:]:
        dados = line.split(',')
        filme = dados[4].strip()  # Coluna '#1 Movie' (posição 4)
        filmes.append(filme)

    # Contar a frequência de cada filme
    contagem_filmes = Counter(filmes)

    # Ordenar os filmes primeiro pela quantidade (decrescente), depois pelo nome (alfabeticamente)
    filmes_ordenados = sorted(contagem_filmes.items(), key=lambda x: (-x[1], x[0]))

    # Escrever a saída no formato solicitado
    for idx, (filme, quantidade) in enumerate(filmes_ordenados, start=1):
        print(f"{idx} - O filme {filme} aparece {quantidade}x  no dataset.")

except FileNotFoundError:
    print(f"Arquivo '{file_path}' nao encontrado.")

""""
Explicação:
Contagem de filmes: Usei a coluna "#1 Movie" (índice 4) para extrair o nome do filme de cada linha e armazená-lo na lista filmes.
Contagem de ocorrências: Usei o objeto Counter da biblioteca collections para contar quantas vezes cada filme aparece.
Ordenação: Ordenei primeiro pela quantidade (em ordem decrescente) e depois alfabeticamente em caso de empate.
Formato da saída: A saída segue o formato solicitado, com a sequência de aparição, o nome do filme e o número de vezes que ele aparece.



poderia fazer a Contagem de filmes usando pandas MAS NAO POSSO
import pandas as pd

# Definir o caminho do arquivo corretamente
file_path = '../actors.csv'

# Carregar o arquivo CSV usando pandas
df = pd.read_csv(file_path)

# Contar quantos filmes únicos existem na coluna '#1 Movie'
filmes_unicos = df['#1 Movie'].nunique()

# Exibir o número de filmes únicos
print(f"Existem {filmes_unicos} filmes únicos na coluna '#1 Movie'.")


Por nao poder usar pandas eu usei os seguintes comando 
"""


# Usei esse codigo para ver quantos filmes tinha, depois adptei ele para oque foi pedido 

print('')
print('')

print(' Usei esse codigo para ver quantos filmes tinha, depois adptei ele para oque foi pedido ')
from collections import Counter

file_path = '../actors.csv'

try:
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Variável para armazenar todos os filmes da coluna '#1 Movie'
    filmes = []

    # Processar cada linha a partir da segunda (ignorando o cabeçalho)
    for line in lines[1:]:
        dados = line.split(',')
        filme = dados[4].strip()  # Coluna '#1 Movie' (posição 4)
        filmes.append(filme)

    # Contar a frequência de cada filme
    contagem_filmes = Counter(filmes)

    # Exibir a contagem dos filmes
    for filme, quantidade in contagem_filmes.items():
        print(f" filme {filme} aparece {quantidade} vez(es).")

except FileNotFoundError:
    print(f"Arquivo '{file_path}' nao encontrado.")


# muito mais facil 😁
print("-----------------------------------------------------------")

print("destacando os filmes que têm a mesma quantidade de aparições:")

file_path = 'actors.csv'

try:
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Dicionário para armazenar os filmes e suas quantidades
    contagem_filmes = {}

    # Processar cada linha a partir da segunda (ignorando o cabeçalho)
    for line in lines[1:]:
        dados = line.split(',')
        filme = dados[4].strip()  # Coluna '#1 Movie' (posição 4)

        # Se o filme já está no dicionário, incrementamos sua contagem
        if filme in contagem_filmes:
            contagem_filmes[filme] += 1
        else:
            # Caso contrário, adicionamos o filme com contagem inicial de 1
            contagem_filmes[filme] = 1

    # Ordenar os filmes pela quantidade (decrescente) e pelo nome em ordem alfabética
    filmes_ordenados = sorted(contagem_filmes.items(), key=lambda x: (-x[1], x[0]))

    # Exibir a saída e identificar empates
    ultimo_quantidade = None  # Variável para armazenar a quantidade do último filme
    for idx, (filme, quantidade) in enumerate(filmes_ordenados, start=1):
        print(f"{idx} - O filme {filme} aparece {quantidade} vez(es) no dataset.")
        
        # Verificar se há empate comparando com a quantidade do último filme
        if quantidade == ultimo_quantidade:
            print(f"  (Empate na quantidade: {quantidade} vezes)")
        
        # Atualizar a variável 'ultimo_quantidade'
        ultimo_quantidade = quantidade

except FileNotFoundError:
    print(f"Arquivo '{file_path}' nao encontrado.")
