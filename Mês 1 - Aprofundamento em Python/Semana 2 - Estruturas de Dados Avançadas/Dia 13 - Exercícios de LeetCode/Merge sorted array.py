'''
Merge Sorted Array
'''

'''

Recebemos duas listras ordenadas nums1 e nums2, e um inteiro m e n, que representam
o número de elementos válidos em cada lista.
O objetivo é mesclar nums2 dentro de nums1, mantendo tudo em ordem crescente. O resultado
deve ser armazenado dentro de nums1, sem criar uma nova lista.

Restrições:
 - nums1 tem tamanho m + n, e os últimos n espaços são preenchidos com 0 (para armazenar os elementos de nums2)
 - A solução deve ser O(m + n) em complexidade de tempo

Exemplo 1:

Entrada:
nums1 = [1, 2, 3, 0, 0, 0], m = 3
nums2 = [2, 5, 6], n = 3

Saída:
nums1 = [1, 2, 2, 5, 6]


Exemplo 2:

Entrada:
nums1 = [1], m = 1
nums2 = [], n = 0

Saída:
num1 = [1]

Objetivo:
 - Criar uma função merge(num 1, m, nums2, n) que mescla os dois arrays diretamente dentro
de nums1 sem usa routra lista


Estratégia para resolver:

Como nums1 já tem espaço extra no final, podemos preencher a lista de trás pra frente, pois
isso evita ter que mover elementos rapidamente, e mantemos a ordem ordenada sem a necessidade
de criar uma nova lista.

Como fazer isso:
Usando três ponteiros:
 1. p1 = m - 1 -> Último elemento válido de nums1
 2. p2 = n - 1 -> Último elemento de nums2
 3. p = m + n - 1 -> Última posição de nums1 (onde o maior elemento será colocado)

 - Comparamos nums1[p1] e nums2[p2] colocanod o maior valor em nums1[p]
 - Repetimos o processo até que nums2 esteja completamente mesclado
 
Implementação:
'''

def merge(nums1, m, nums2, n):
    p1, p2, p = m - 1, n - 1, m + n - 1 #inicializando ponteiros

    while p2 >= 0: #precisamos garantir que todos os elementos de nums2 sejam inseridos
        if p1 >= 0 and nums1[p1] > nums2[p2]:
            nums1[p] = nums1[p1] #move o maior valor para a posição correta
            p1 -= 1 #move o ponteiro de nums1 pra esquerda
        else:
            nums1[p] = nums2[p2] #insere um elemento de nums2
            p2 -= 1 #move o ponteiro de nums2 para a esquerda
        p -= 1 #move a posição de inserção para a esquerda

'''
Explicação do código:

1 - Inicializando os ponteiros:
 - p1 aponta para o último número válido de nums1
 - p2 aponta para o último número de nums2
 - p aponta para o último espaço disponível em nums1

2 - Loop principal (while p2 >= 0):
 - Se p1 >= 0 e nums1[p1] > nums2[p2]:
   - copia nums1[p1] para nums1[p] e move p1 para a esquerda

 Senão:
  - Copia nums2[p2] para nums1[p] e move p2 para a esquerda

 - Em ambos os casos movemos p para uma posição à esquerda
 
3 - O loop para quando todos os elementos de nums2 forem inseridos (porque nums1 já contém os
valores ordenados no início)


Testando o código:

Vamos testar os seguintes exemplos:
'''

nums1 = [1, 2, 3, 0, 0, 0]
m = 3

nums2 = [2, 5, 6]
n = 3

merge(nums1, m, nums2, n)
print(nums1) #[1, 2, 2, 3, 5, 6]


nums1 = [1]
m = 1

nums2 = []
n = 0

merge(nums1, m, nums2, n)
print(nums1) #[1]

'''
Complexidade:

 - Como percorremos os elementos de nums1 e nums2 apenas uma vez, temos O(m + n)
 - Não usamos listas auxiliares, apenas manipulamos os ponteiros, tornando a solução eficiente
em memória.
'''