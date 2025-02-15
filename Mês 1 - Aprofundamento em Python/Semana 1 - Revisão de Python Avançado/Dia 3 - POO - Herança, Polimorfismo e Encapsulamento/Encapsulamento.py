'''
Encapsulamento -
 - Controla o acesso aos atributos e métodos de uma classe
 - Protege os dados e impede alterações indevidas
 - Modificadores de Acesso:
    - Público (self.atributo): Acesso livre
    - Protegido (self._atributo): Indica que não deve ser alterado diretamente
    - Privado (self.__atributo): Só pode ser acessado dentro da própria classe
'''

class ContaBancaria:
    def __init__(self, saldo):
        self.__saldo = saldo #atributo privado (__)

    def depositar(self, valor):
        self.__saldo += valor

    def obter_saldo(self):
        return self.__saldo

conta = ContaBancaria(1000)
conta.depositar(500)
print(conta.obter_saldo())