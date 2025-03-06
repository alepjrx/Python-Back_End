'''
 - Algoritmo 2 - Selection Sort

 O selection sort funciona escolhendo o menor elemento da lista e colocando-o na posição
correta.
 Ideia principal: Seleciona o menor número e coloca no início.

 Passo a passo:
 1 - Encontra o menor elemento da lista
 2 - Troca esse elemento com o primeiro da lista
 3 - Repete o processo com o restante da lista (ignorando os que já foram organizados)
'''
# código de Selection Sort:

def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        min_index = i  # assume que o menor elemento está na posição i
        for j in range(i + 1, n):  # procura um elemento menor
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]  # troca


# teste
arr = [8, 64, 32, 16, 4, 128, 256]
selection_sort(arr)
print('Selection sort: ')
print(arr)  # 4, 8, 16, 32, 64, 128, 256