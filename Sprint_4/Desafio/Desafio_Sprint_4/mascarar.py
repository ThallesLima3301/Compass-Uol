def mascarar_palavras(texto):
    
    # Substitui as vogais nas palavras por '*'
    palavras = texto.split()
    mascaradas = [''.join('*' if letra.lower() in 'aeiou' else letra for letra in palavra) for palavra in palavras]
    return ' '.join(mascaradas)

input_texto = input("Digite um texto para mascarar: ")

resultado = mascarar_palavras(input_texto)

print(f"Texto mascarado: {resultado}")

