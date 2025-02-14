'''
O encapsulamento é um dos pilares da POO e serve pra controlar o acesso dos atributos e métodos de uma classe,
protegendo os dados.

1- Modificadores de acesso em Python:

Em Python, existem três níveis de acesso para atributos e métodos:

Público (public) - Pode ser acessado de qualquer lugar
Protegido (protected) - Deve ser acessado apenas dentro da classe e subclasses (convenciona-se com _)
Privado (private) - Só pode ser acessado dentro da própria classe (convenciona-se com __)
'''

#Exemplo de Encapsulamento:

class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular #atributo público
        self._saldo = saldo #atributo protegido
        self.__senha = '0000' #atributo privado

    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            print(f'Depósito de R${valor:.2f} realizado. Saldo atual: R${self._saldo:.2f}')
        else:
            print('Valor inválido para depósito.')

    def sacar(self, valor):
        if 0 < valor <= self._saldo:
            self._saldo -= valor
            print(f'Saque de R${valor:.2f} realizado. Saldo atual: R${self._saldo:.2f}.')
        else:
            print('Saldo insuficiente ou valor inválido.')

    def exibir_saldo(self):
        print(f'Saldo disponível: R${self._saldo:.2f}')

#criando a conta
conta = ContaBancaria('João', 1000)

#utilizando os métodos
conta.depositar(750.00)
conta.exibir_saldo()

conta.sacar(800.00)
conta.exibir_saldo()

#acessando atributos diretamente
print(conta.titular) #mostra o titular da conta (Atributo Público)
print(conta._saldo) #exibe o aviso: "weak warning: Access to a protected member _saldo of a class" (Protegido (protected))
print(conta.__senha) #nem funciona, dá erro de atributo (Privado (private))