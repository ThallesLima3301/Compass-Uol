"""
Implemente duas classes, Pato e Pardal , que herdam de uma superclasse chamada Passaro as habilidades de voar e emitir som.


Contudo, tanto Pato quanto Pardal devem emitir sons diferentes (de maneira escrita) no console, conforme o modelo a seguir.


Imprima no console exatamente assim:

    Pato
    Voando...
    Pato emitindo som...
    Quack Quack
    Pardal
    Voando...
    Pardal emitindo som...
    Piu Piu
"""

class Passaro:
    def voar(self):
        print("Voando...")
    
    def emitir_som(self):
        raise NotImplementedError("dasda.")

class Pato(Passaro):
    def emitir_som(self):
        print("Quack Quack")

class Pardal(Passaro):
    def emitir_som(self):
        print("Piu Piu")

# Criando instâncias e chamando os métodos
pato = Pato()
print("Pato")
pato.voar()
print("Pato emitindo som...")
pato.emitir_som()

pardal = Pardal()
print("\nPardal")
pardal.voar()
print("Pardal emitindo som...")
pardal.emitir_som()
