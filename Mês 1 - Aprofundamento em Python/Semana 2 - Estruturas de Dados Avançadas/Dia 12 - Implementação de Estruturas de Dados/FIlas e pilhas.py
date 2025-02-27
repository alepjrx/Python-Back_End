'''
Filas e Pilhas

Agora, vamos implementar essas estruturas sem usar deque do Python.
'''

'''
Pilha (stack)
Segue a regra LIFO (Last In, First Out): O último elemento a entrar é o primeiro a sair.
'''

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, value): #empilha um elemento
        self.stack.append(value)

    def pop(self): #remove e retorna o elemento ao topo
        if not self.is_empty():
            return self.stack.pop()
        return 'Stack Vazia'

    def peek(self): #retorna o elemento do topo sem remover
        return self.stack[-1] if not self.is_empty() else 'Stack Vazia'

    def is_empty(self): #verifica se a stack está vazia
        return len(self.stack) == 0

    def size(self): #retorna o tamanho da pilha
        return len(self.stack)

#testando a pilha
s = Stack()
s.push(5)
s.push(10)
s.push(15)
print(s.pop()) #imprime 15
print(s.peek()) #imprime 10


'''
Fila (Queue)
Segue a regra FIFO (First In, First Out): O primeiro a entrar é o primeiro a sair.
'''

class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, value): #adiciona um elemento ao final da fila
        self.queue.append(value)

    def dequeue(self): #remove e retorna o primeiro elemento
        if not self.is_empty():
            return self.queue.pop(0)
        return 'Queue(Fila) Vazia'

    def peek(self): #retorna o primeiro elemento sem remover
        return self.queue[0] if not self.is_empty() else 'Queue(fila) vazia'

    def is_empty(self): #verifica se a fila está vazia
        return len(self.queue) == 0

    def size(self): #retorna o tamanho da fila
        return len(self.queue)

#testando a fila
q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print(q.enqueue()) #deve imprimir 1
print(q.peek()) #deve imprimir 2