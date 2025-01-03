
"""
Implemente a função my_map(list, f) que recebe uma lista como primeiro argumento e uma função como segundo argumento. Esta função aplica a função recebida para cada elemento da lista recebida e retorna o resultado em uma nova lista.


Teste sua função com a lista de entrada [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] e com uma função que potência de 2 para cada elemento.
"""

# Implementando a função my_map
def my_map(lst, f):
    return [f(item) for item in lst]

# Testando a função com a lista e uma função que retorna a potência de 2
lista_teste = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
resultado = my_map(lista_teste, lambda x: x ** 2)

# Garantindo que a saída seja impressa corretamente no formato esperado
print(resultado)
