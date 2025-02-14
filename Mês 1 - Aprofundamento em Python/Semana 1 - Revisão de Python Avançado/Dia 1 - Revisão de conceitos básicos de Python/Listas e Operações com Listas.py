lista_1 = [0, 5, 8, 13, 4, 21]
print(f'A lista inicial é:\n{lista_1}\n')

tamanho = len(lista_1) #len() diz a quantidade de indexes na lista
print(f'A lista contém {tamanho} indexes\n')

lista_1.append(7) #.append() adiciona um valor ao final da lista
print(f'Primeira modificação: Adicionar um valor ao final da lista, no caso, número 7 -\n{lista_1}\n')

lista_1.remove(4) #.remove() remove um número especificado da lista
print(f'Segunda modificação: Remover um valor especificado da lista, no caso, número 4 -\n{lista_1}\n')

lista_1.sort() #.sort() organiza em ordem crescente
print(f'Organizar a lista em ordem crescente -\n{lista_1}\n')
