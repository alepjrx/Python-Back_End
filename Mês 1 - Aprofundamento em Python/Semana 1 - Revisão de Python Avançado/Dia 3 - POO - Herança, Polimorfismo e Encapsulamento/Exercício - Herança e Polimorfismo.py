'''
Exercícios - Herança e Polimorfismo
 - Criar uma classe (Veículo) e duas subclasses (Carro e Moto), implementando herança
e polimorfismo
'''

class Veiculo:
    def __init__(self, nome):
        self.nome = nome

    def quantidade_rodas(self):
        pass

class Carro(Veiculo):
    def quantidade_rodas(self):
        return '4'

class Moto(Veiculo):
    def quantidade_rodas(self):
        return '2'

veiculos = [Carro('Ford'), Moto('Honda')]

for veiculo in veiculos:
    print(veiculo.quantidade_rodas())