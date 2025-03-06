'''
 - Algoritmo 3 - Insertion Sort

 O insertion sort funciona inserindo elementos na posição correta, somo se estivéssemos
organizando cartas na mão.
 Ideia principal: Cada novo elemento é inserido no local correto da parte já ordenada da lista.

 Passo a passo:
 1 - Começa no segundo elemento pois assume que o primeiro já está ordenado
 2 - Compara o elemento atual com os anteriores, movendo-os para abrir espaço se necessário
 3 - Insere o elemento no local correto
 4 - Repete o processo até que todos os elementos estejam na posição correta
'''
# código de Insertion Sort:

def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):  # começa do segundo elemento
        key = arr[i]  # elemento que será inserido na posição correta
        j = i - 1
        while j >= 0 and arr[j] > key:  # move elementos maiores para frente
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key  # insere na posição correta


# teste
arr = [3, 1, 21, 0, 8, 5, 13, 2]
insertion_sort(arr)
print('Insertion sort: ')
print(arr)  # 0, 1, 2, 3, 5, 8, 13, 21