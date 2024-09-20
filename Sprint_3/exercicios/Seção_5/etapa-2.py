# etapa-2.py
"""
Plano:
Ler o arquivo CSV e extrair a coluna "Total Gross".
Somar os valores dessa coluna.
Calcular a média dividindo a soma total pelo número de atores (linhas).
Imprimir o resultado.
Pseudocódigo:
Abrir o arquivo CSV.
Pular o cabeçalho.
Iterar pelas linhas para extrair a coluna "Total Gross".
Somar os valores e contar quantas entradas foram processadas.
Dividir a soma pelo total de entradas e exibir a média.
"""

file_path = '../actors.csv'

try:
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Variáveis para armazenar a soma total e a contagem de atores
    soma_gross = 0
    contagem_atores = 0

    # Processar cada linha e calcular a soma e a média da coluna 'Gross'
    for line in lines[1:]:  # Ignorar o cabeçalho
        dados = line.split(',')
        try:
            gross = float(dados[5].strip())  # Pegar a coluna 'Gross' (coluna 5)
            soma_gross += gross
            contagem_atores += 1
        except ValueError:
            continue

    # Calcular a média
    if contagem_atores > 0:
        media_gross = soma_gross / contagem_atores
        print(f"A media da receita bruta (Gross) e: {media_gross:.2f} milhoes de dolares.")
    else:
        print("Nenhum dado de receita bruta encontrado.")

except FileNotFoundError:
    print(f"Arquivo '{file_path}' nao encontrado.")