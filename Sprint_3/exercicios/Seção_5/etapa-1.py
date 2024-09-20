""" 
Leitura do arquivo: O arquivo actors.csv é aberto e lido linha por linha.

Contagem dos filmes: A coluna "Number of Movies" (posição 2 no arquivo CSV) é convertida para um inteiro e comparada com o valor máximo atual. Se for maior, o valor é atualizado.

Bloco try-except: Se ocorrer um erro, como o arquivo não ser encontrado ou um valor inválido na conversão, o programa captura esse erro e exibe uma mensagem, mas continua rodando.
Resultado: Exibe o ator/atriz com o maior número de filmes e a quantidade.
""" 
# etapa-1.py

# Definir o caminho do arquivo corretamente
file_path = '../actors.csv'

# abrir o arquivo e processar os dados
try:
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Variáveis para armazenar o ator com o maior número de filmes
    max_filmes = 0
    ator_mais_filmes = ''

    # Processar cada linha a partir da segunda (ignorando o cabeçalho)
    for line in lines[1:]:
        dados = line.split(',')
        ator = dados[0].strip()  # Coluna 'Actor' com strip para remover espaços extras
        try:
            filmes = int(dados[2].strip())  # Coluna 'Number of Movies' (posição 2)
            if filmes > max_filmes:
                max_filmes = filmes
                ator_mais_filmes = ator
        except ValueError:
            # Se houver algum valor inválido, o programa continua
            continue

    # Exibir o resultado
    print(f"O ator/atriz com o maior numero de filmes e {ator_mais_filmes}, com {max_filmes} filmes.")

except FileNotFoundError:
    print(f"Arquivo '{file_path}' nao encontrado. Verifique o caminho.")
