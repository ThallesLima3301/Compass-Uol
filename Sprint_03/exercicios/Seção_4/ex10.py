"""
Exercícios Parte 2

Escreva uma função que recebe uma lista e retorna uma nova lista sem elementos duplicados. Utilize a lista a seguir para testar sua função.


['abc', 'abc', 'abc', '123', 'abc', '123', '123'] 

"""


def remove_duplicatas(lista):
    return list(set(lista))

lista_teste = ['abc', 'abc', 'abc', '123', 'abc', '123', '123']

lista_sem_duplicatas = remove_duplicatas(lista_teste)

print(lista_sem_duplicatas)
