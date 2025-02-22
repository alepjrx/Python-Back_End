'''
Conjuntos armazenam elementos únicos e não ordenados
'''

#criando um conjunto
numeros = {1, 2, 3, 4, 5}
numeros.add(6) #adicionando o elemento
numeros.remove(3) #remove o elemento

#união e interseção
outros_numeros = {4, 5, 6, 7, 8}
print(numeros | outros_numeros) #união
print(numeros & outros_numeros) #interseção