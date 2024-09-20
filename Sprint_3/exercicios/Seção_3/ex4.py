"""
Escreva um código Python para imprimir todos os números primos entre 1 até 100. Lembre-se que você deverá desenvolver o cálculo que identifica se um número é primo ou não.


Importante: Aplique a função range().
"""

# Função para verificar se um número é primo
def eh_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# Percorrer todos os números de 1 a 100
for numero in range(1, 101):
    if eh_primo(numero):
        print(numero)
