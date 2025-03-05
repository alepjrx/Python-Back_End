'''
Exercício de Remove Element de nível fácil-médio do LeetCode, focado em estrutura de dados e
algoritmos de busca.
'''

'''
Exercício: Remove Element

Dado um array de núumeros inteiros (nums) e um número inteiro (val), remova todas as ocorrências
de (val) no array in-place, ou seja, sem criar um novo array, e retorne o novo tamanho do array.


Restrições:
- 0 <= nums.lenght <= 100
- 0 <= nums[i] <= 50
- 0 <= val <= 50

Exemplo 1:

Entrada: nums = [3, 2, 2, 3], val = 3
Saída: 2
Explicação: O array se torna [2, 2, _, _] (os _ representam os valores que foram ignorados)

Exemplo 2:

Entrada: nums = [0, 1, 2, 2, 3, 0, 4, 2], val = 2
Saída: 5
Explicação: O array se torna [0, 1, 4, 0, 3, _, _, _]


Objetivo:
 - Implementar uma função remove_element(nums, val) -> int que remove os elementos val do
array e retorna o novo tamamho da lista
 - A solução deve ser O(n) em complexidade de tempo



Passo 1 - Compreender o problema:

Temos uma lista (nums) e queremos remover todas as ocorrências de um número específico (val).
 - Devemos modificar a lista no próprio local (in-place) sem criar outra lista
 - No final, precisamos retornar o novo tamanho da lista após a remoção dos elementos val


Passo 2 - Estratégia para resolver

Podemos usar dois ponteiros:
 - Um ponteiro (i) percorre a lista inteira, verificando cada elemento
 - Outro ponteiro (j) mantém os elementos válidos (ou seja, aqueles que não são (val))


Passo 3 - Implementação

Vamos criar a função e adicionar os ponteiros:
'''

def remove_element(nums, val):
    j = 0 #ponteiro que armazena a posição dos elementos válidos (que não são (val))

    for i in range(len(nums)): #for loop na lista inteira pra percorrer ela toda
        if nums[i] != val: #se for diferente (!=) de val
            nums[j] = nums[i] #move o elemento válido para a posição de j
            j += 1

    return j #mostra o novo tamanho da lista

'''
Passo 4 - Explicação do código
 - Criamos um ponteiro j para armazenar os elementos que não são (val)
 - Percorremos (nums) com (i) e, se (nums[i]) não for igual a (val), copiamos para (nums[j])
 - No final, (j) conterá o novo tamanho do array
 

Passo 5 - Testando o código

Testanto com os exemplos fornecidos:
'''

nums1 = [3, 2, 2, 3]
val1 = 3
print(remove_element(nums1, val1)) #aparecerá 2

nums2 = [0, 1, 2, 2, 3, 0, 4, 2]
val2 = 2
print(remove_element(nums2, val2)) #aparecerá 5

'''
Eu falei com o Chat GPT que sentia que devem existir formas mais fáceis de resolver
esse problema, pois esse método, embora pareça muito eficiente, me dá a sensação de
ser uma forma mais trabalhosa do que outras. Ele respondeu que sim, há outras formas
como o uso de .remove() ou utilizando list comprehension, mas a forma de dois pontos
é a melhor em questão de desempenho.
'''

#forma utilizando list comprehension apenas para praticar:

def remove_element(nums, val):
    nums[:] = [x for x in nums if x != val] #mantém apenas os números diferentes de vel
    return len(nums) #retorna o novo tamanho

'''
Entendo quando ele disse que a forma de dois pontos é a melhor em questão de desempenho,
mas essa forma me pareceu mais "legível" como ser humano, e eu consigo entender melhor
dígito por dígito o que está acontecendo.
'''