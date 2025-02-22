class Funcionario:
    def __init__(self, nome, cargo, salario):
        self.nome = nome
        self.cargo = cargo
        self.salario = salario

    def exibir_detalhes(self):
        print(f'Nome: {self.nome}, cargo: {self.cargo}, salário: {self.salario:.2f}.'
              )

    def aumentar_salario(self, percentual):
        self.salario *= (1 + percentual / 100)
        print(f'Salário de {self.nome} aumentado em {percentual}%, Novo salário: R$ {self.salario:.2f}')

    def promover(self, novo_cargo, novo_salario):
        self.cargo = novo_cargo
        self.salario = novo_salario
        print(f'{self.nome} foi promovido(a) para {self.cargo} com novo salário de R$ {self.salario:.2f}')


funcionario1 = Funcionario('João', 'Gerente', 2000.00)
funcionario2 = Funcionario('Maria', 'Vendedora', 1500.00)

funcionario1.exibir_detalhes()
funcionario1.aumentar_salario(15)

funcionario2.promover('Coordenador(a)', 3000.00)