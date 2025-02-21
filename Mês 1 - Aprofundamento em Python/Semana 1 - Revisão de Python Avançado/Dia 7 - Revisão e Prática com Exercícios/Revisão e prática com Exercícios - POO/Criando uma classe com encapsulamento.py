class ContaBancaria:
    def __init__(self, saldo=0): #aqui devemos sempre iniciar com ZERO saldo na conta
        self.__saldo = saldo

    def depositar(self, valor):
        self.__saldo += valor

    def sacar(self, valor):
        self.__saldo -= valor

    def ver_saldo(self):
        return self.__saldo

conta = ContaBancaria()

conta.depositar(500)
print(f'Seu saldo atual é de: R$ {conta.ver_saldo()}')

conta.sacar(200)
print(f'Seu saldo atual é de: R$ {conta.ver_saldo()}')
