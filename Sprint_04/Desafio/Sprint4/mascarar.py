import hashlib
def gerar_hash_sha1(texto):
    hash_object = hashlib.sha1(texto.encode())
    return hash_object.hexdigest()

def exibir_menu():
    print("\n=== Menu de Opções ===")
    print("1 - Gerar Hash SHA-1")
    print("2 - Sair")
    opcao = input("Escolha uma opção: ")
    return opcao

while True:
    opcao = exibir_menu()
    
    if opcao == "1":
        input_string = input("Digite uma string para gerar o hash SHA-1e mascarar: ")
        hex_dig = gerar_hash_sha1(input_string)
        print(f"O hash SHA-1 da string '{input_string}' é: {hex_dig}")
    
    elif opcao == "2":
        print("Finalizando o programa...")
        break
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")