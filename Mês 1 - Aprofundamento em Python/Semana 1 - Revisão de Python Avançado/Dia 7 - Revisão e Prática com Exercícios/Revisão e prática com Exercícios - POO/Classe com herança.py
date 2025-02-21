class Carro:
    def __init__(self, marca, modelo, ano, bateria):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.bateria = bateria

    def descricao(self):
        print(f'Marca: {self.marca}, modelo: {self.modelo}, ano: {self.ano}, bateria: {self.bateria}')

    def autonomia(self):
        print(f'A autonomia do carro é de {5 * self.bateria} KMs')


meu_carro_eletrico = Carro('Tesla', 'Model 3', 2022, 75)

print(meu_carro_eletrico.descricao())
print(meu_carro_eletrico.autonomia())