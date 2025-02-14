class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.ligado = False

    def ligar(self):
        if not self.ligado:
            self.ligado = True
            print(f'O carro {self.modelo} está agora ligado.')
        else:
            print(f'O carro {self.modelo} já está ligado')

    def desligar(self):
        if self.ligado:
            self.ligado = False
            print(f'O carro {self.modelo} foi desligado.')
        else:
            print(f'O carro {self.modelo} já está desligado.')


meu_carro = Carro('Mazda', '787B', 1991) #objeto da classe Carro


meu_carro.ligar() #métodos do objeto
meu_carro.ligar()
meu_carro.desligar()
meu_carro.desligar()