"""
Leia o arquivo person.json, faça o parsing e imprima seu conteúdo.

Dica: leia a documentação do pacote json
"""

import json

with open('person.json', 'r') as arquivo_json:
    dados = json.load(arquivo_json)

print(dados)
