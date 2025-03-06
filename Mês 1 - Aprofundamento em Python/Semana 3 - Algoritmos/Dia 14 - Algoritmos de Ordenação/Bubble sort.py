'''
O que é um algoritmo de Ordenação?
'''

'''
 É um método usado para organizar elementos em uma sequência crescente ou decrescente.
 Os três algoritmos que vamos ver tem complexidade O(n²) no pior caso, ou seja, não
são os mais eficientes para grandes volumes de dados, no entanto, são excelentes para aprender
os princípios básicos da ordenação.

 - Algoritmo 1 - Bubble Sort
 
 O bubble sort funciona comparando pares de elementos adjacentes e trocando-os se estiverem
fora de ordem.
 Ideia principal: Os maiores valores subindo até o fim da lista, como bolhas em copos dágua (?????)
 
 Passo a passo:
 1 - Percorre a lista rapidamente
 2 - Compara cada par de elementos adjacentes e troca se estiverem fora de ordem
 3 - Após cada iteração, o maior elemento "bolha" para sua posição final
 4 - Repete o processo até que não haja mais trocas
'''
#código bubble sort:

def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1): #percorre toda a lista (n-1 vezes)
        swapped = False
        for j in range(n - i - 1): #últimos elementos já estão ordenados
            if arr[j] > arr[j + 1]: #se estiverem fora de ordem, troca
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break #se não há mais trocas, a lista já está ordenada

#teste
arr = [32, 45, 78, 12, 7, 33, 84]
bubble_sort(arr)
print('Bubble sort:')
print(arr) #7, 12, 32, 33, 45, 78, 84

'''
Comparação entre os algoritmos:

 - Bubble Sort é simples mas muito ineficiente
 - Selection Sort reduz trocas, mas ainda é O(n²)
 - Insertion Sort é ótimo quando a lista já está quase ordenada
'''