"""
apresentar a lista dos atores ordenada pela receita bruta de bilheteria dos seus filmes (coluna "Total Gross") em ordem decrescente, 
e depois salvar essa lista em um arquivo seguindo o padrão:
(nome)- (receita total bruna)

Plano:
Ler o arquivo actors.csv.
Extrair o nome do ator e o valor da coluna "Total Gross".
Ordenar os atores pela "Total Gross" em ordem decrescente.
Escrever a lista ordenada em um arquivo de texto, no formato solicitado.

"""

file_path = '../actors.csv'
output_file = 'atores_total_gross.txt'

try:
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Variável para armazenar o nome do ator e a receita bruta total
    atores_total_gross = []

    # Processar cada linha a partir da segunda (ignorando o cabeçalho)
    for line in lines[1:]:
        dados = line.strip().split(',')
        
        # Verificar se a linha tem o número correto de colunas (6 colunas no total)
        if len(dados) < 6:
            continue  # Ignorar linhas com colunas faltando

        ator = dados[0].strip()  # Coluna 'Actor' (posição 0)
        
        try:
            total_gross = float(dados[1].strip())  # Coluna 'Total Gross' (posição 1)
        except ValueError:
            continue  # Pular a linha se o valor não puder ser convertido

        # Adicionar o ator e o "total_gross" à lista
        atores_total_gross.append((ator, total_gross))

    # Ordenar pela receita bruta total em ordem decrescente
    atores_total_gross.sort(key=lambda x: x[1], reverse=True)

    # Escrever no arquivo de saída no formato especificado
    with open(output_file, 'w') as output:
        for ator, total_gross in atores_total_gross:
            output.write(f"{ator} - {total_gross:.2f}\n")

    print(f"Arquivo '{output_file}' gerado com sucesso.")

except FileNotFoundError:
    print(f"Arquivo '{file_path}' nao encontrado.")


"""

eu achei mais legal de ler assim, mas vc me obrigaram a fazer "(nome do autor)- (receita total bruna)"
 with open(output_file, 'w') as output:
        output.write("Lista dos atores com maior receita bruta de bilheteria:\n\n")
        for ator, total_gross in atores_total_gross:
            output.write(f"{ator}: ${total_gross:.2f} milhoes\n")

    print(f"Arquivo '{output_file}' gerado com sucesso.")
"""