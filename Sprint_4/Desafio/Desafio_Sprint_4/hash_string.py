import hashlib

input_string = input("Digite uma string para gerar o hash SHA-1: ")

hash_object = hashlib.sha1(input_string.encode())

hex_dig = hash_object.hexdigest()
print(f"O hash SHA-1 da string '{input_string}' é: {hex_dig}")
