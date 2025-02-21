class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def descricao(self):
        print(f'Marca: {self.marca}, modelo: {self.modelo}, ano: {self.ano}.')

    def idade(self):
        print(f'O carro tem {2025 - self.ano} anos.')

meu_carro = Carro('Ferrari', '458 Italia', 2009)

print(meu_carro.descricao())
print(meu_carro.idade())