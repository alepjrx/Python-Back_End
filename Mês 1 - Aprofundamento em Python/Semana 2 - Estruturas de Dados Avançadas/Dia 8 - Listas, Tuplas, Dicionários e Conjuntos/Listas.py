'''
Listas
 Uma lista é uma coleção ordenada e mutável de elementos. Ela pode armazenar diferentes tipos de dados.
'''

#criando a lista
frutas = ['maçã', 'banana', 'uva']
print(frutas)

#manipulando - adicionando elementos
frutas.append('laranja') #append adiciona ao final
frutas.insert(1, 'manga') #define o index e adiciona o objeto ao index definido

#manipulando - removendo elementos
frutas.remove('uva') #remove pelo valor dado (int, str...)
frutas.pop(2) #remove pelo index

print(frutas)