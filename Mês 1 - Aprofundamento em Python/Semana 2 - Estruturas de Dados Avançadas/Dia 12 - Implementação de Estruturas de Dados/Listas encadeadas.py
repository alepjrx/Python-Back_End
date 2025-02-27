'''
Listas Encadeadas

Diferente das listas do Python (list), que são implementadas como arrays dinâmicos, as listas
encadeadas usam nós conectados entre si, cada um contendo um valor e uma referência para o próximo nó.

Lista Encadeada Simples:
Cada nó contém:
 - Valor
 - Ponteiro para o próximo nó
'''

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None #primeiro nó da lista

    def append(self, value): #adiciona um novo nó ao final da lista
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def display(self): #exibe os valores da lista
        current = self.head
        while current:
            print(current.value, end=' -> ')
            current = current.next
        print('None')


#testando a lista encadeada:
ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.display() #deve imprimir 1 -> 2 -> 3 -> None

'''
Lista Duplamente Encadeada
 - Cada nó agora contém um ponteiro para o próximo e anterior nó
'''

class DoubleNode:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, value): #adiciona um novo nó ao final
        new_node = DoubleNode(value)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
            new_node.prev = current

    def display_forward(self): #percorre a lista na ordem normal
        current = self.head
        while current:
            print(current.value, end=' <-> ')
            current = current.next
        print('None')

#testando a lista duplamente encadeada
dll = DoublyLinkedList()
dll.append(10)
dll.append(20)
dll.append(30)
dll.display_forward() #deve imprimir: 10 <-> 20 <-> 30 <-> None