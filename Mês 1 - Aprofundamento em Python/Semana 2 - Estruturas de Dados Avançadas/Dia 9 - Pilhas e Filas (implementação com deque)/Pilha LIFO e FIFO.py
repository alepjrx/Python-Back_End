'''
Pilha LIFO (Last in, first out)

A pilha segue o princípio do último ao entrar, primeiro a sair. No deque usamos:
 - append() para adicionar um elemento ao topo da pilha
 - pop() para remover o elemento do topo
'''

from collections import deque

pilha = deque()

#adicionando elementos:
pilha.append('A')
pilha.append('B')
pilha.append('C')

print('Pilha:', pilha)

#removendo elementos:
pilha.pop()
print('Após remover o topo:', pilha)

'''
Visualizar uma pilha de objetos torna mais fácil a compreensão do funcionamento: quando se adiciona um
objeto ao topo de uma pilha, para retirar, se retira o último objeto adicionado, pois é impossível
retirar o primeiro pois ele está embaixo de todos os outros objetos.
'''


'''
Fila (FIFO - First in, first out)

A fila segue o princípio do primeiro a entrar, primeiro a sair. No deque, usamos:
 - append() para adicionar elementos ao final da fila
 - popleft() para remover o primeiro elemento
'''

fila = deque()

#adicionando elementos:
fila.append('X')
fila.append('Y')
fila.append('Z')

print('Fila:', fila)

#removendo elementos:
fila.popleft()
print('Após remover o primeiro elemento:', fila)

'''
A visualização desse método também o facilita: em uma fila se atende, ou retira da fila, o primeiro
que chegou e depois o segundo e assim continua...
'''