"""
Escreva uma função que recebe uma string de números separados por vírgula e retorne a soma de todos eles. Depois imprima a soma dos valores.


A string deve ter valor  "1,3,4,6,10,76"
"""

def soma_numeros(string_numeros):
    # Divide a string em números e converte cada um para inteiro
    numeros = [int(num) for num in string_numeros.split(',')]
    # Retorna a soma dos números
    return sum(numeros)

# String com os números
string = "1,3,4,6,10,76"
# Calcula a soma
resultado = soma_numeros(string)

# Imprime apenas o resultado
print(resultado)
