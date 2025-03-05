import datetime
ano_atual = datetime.datetime.now().year

class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def descricao(self):
        print(f'Marca: {self.marca}, modelo: {self.modelo}, ano: {self.ano}.')

    def idade(self):
        print(f'O carro tem {ano_atual - self.ano} anos.')

meu_carro = Carro('Ferrari', '458 Italia', 2009)

print(f'O ano atual é {ano_atual}')
meu_carro.descricao()
meu_carro.idade()