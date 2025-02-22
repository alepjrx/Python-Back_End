'''
Tuplas
 As tuplas são semelhantes às listas, mas são imutáveis (não podem ser alteradas após a criação)
'''

#criando a tuplas
cores = ('vermelho', 'verde', 'azul')
print(cores[0]) #imprime apenas o index definido dentro da tupla

#tentar modificar (vai dar erro)
cores[1] = 'amarelo'

#saída: TypeError: 'tuple' object does not support item assignment
