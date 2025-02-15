'''
Polimorfismo -
 - Objetos diferentes podem ter métodos com o mesmo nome
 - Exemplo de polimorfismo com o método (fazer_som()) em classes diferentes
'''

from Herança import Animal, Cachorro #importar classes do outro módulo

class Gato(Animal):
    def fazer_som(self):
        return "Miau!"

animais = [Cachorro('Rex'), Gato ('Mimi')]

for animal in animais:
    print(animal.fazer_som())