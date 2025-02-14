class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        print(f'Olá, meu nome é {self.nome} e tenho {self.idade} anos de idade')

pessoa1 = Pessoa('João', 25) #objeto da classe Pessoa

pessoa1.apresentar() #utilizando o método apresentar