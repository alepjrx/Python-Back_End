'''
Simulando uma fila de atendimento

Implemente uma classe chamada FilaAtendimento, que representa uma fila de clientes em um atendimento bancário.
A classe deve ter os seguintes métodos:
1 - chegar_cliente(nome) adiciona um novo cliente à fila
2 - chamar_cliente() remove o atual e exibe o próximo cliente a ser atendido. Se a fila estiver vazia, exiba uma mensagem que informe.
3 - exibir_fila() exibe todos os clientes na fila na ordem correta
4 - esvaziar_fila() remove todos os clientes da fila
'''

from collections import deque

class FilaAtendimento:
    def __init__(self):
        self.fila = deque() #criar uma fila com deque
        self.contador = 0 #contador de clientes

    def chegar_cliente(self, nome):
        self.contador += 1 #aumenta o número de clientes
        cliente = (self.contador, nome)
        self.fila.append(nome) #adiciona o cliente ao final da lista
        print(f'O(a) cliente {cliente} entrou na fila.')

    def chamar_cliente(self):
        if self.fila:
            cliente = self.fila.popleft() #remove o primeiro cliente da fila (chama para ser atendido)
            print('\nPróximo cliente.')
            print(f'Atendendo {cliente}')
        else:
            print('\nNenhum cliente na fila.\n')

    def exibir_fila(self):
        if self.fila:
            print('\nFila de Atendimento:')
            for cliente in self.fila: #faz um for loop que imprime todos os nomes na fila
                print(cliente)
        else:
            print('A fila está vazia.')

    def esvaziar_fila(self):
        self.fila.clear() #remove todos os clientes da fila
        print('\nA fila foi esvaziada.')

#testar a fila de atendimento criada

fila = FilaAtendimento()

fila.chegar_cliente('Ana')
fila.chegar_cliente('Bruno')
fila.chegar_cliente('Carlos')

fila.exibir_fila()

fila.chamar_cliente()

fila.exibir_fila()

fila.chamar_cliente()
fila.chamar_cliente()
fila.chamar_cliente() #para testar com a fila vazia

fila.chegar_cliente('Daniel')
fila.exibir_fila()
fila.esvaziar_fila()

fila.exibir_fila()