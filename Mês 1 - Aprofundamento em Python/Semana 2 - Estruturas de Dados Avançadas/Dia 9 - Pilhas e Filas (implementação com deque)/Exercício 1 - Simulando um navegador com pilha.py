'''
Simulando um navegador com Pilha

Crie um programa que simule a navegação em um navegador da web. Ele deve permitir:
 - Acessar uma nova página
 - Voltar para a página anterior
 - Mostrar o histórico de navegação
'''

'''
Lógica da Implementação:

1 - Criamos uma pilha (deque) para armazenar as páginas acessadas.
2 - Permitimos adicionar novas páginas à pilha
3 - Permitimos "voltar" para a página anterior (removendo o topo da pílha)
4 - Exibimos o histórico de navegação
'''

from collections import deque

class Navegador:
    def __init__(self):
        self.historico = deque() #pilha para armazenar as páginas visitadas

    def acessar_pagina(self, url):
        self.historico.append(url)
        print(f'Acessando: {url}')

    def voltar_pagina(self):
        if len(self.historico) > 1: #tem que ter mais que uma página, senão, não há para o que voltar
            self.historico.pop()
            print(f'\nVoltando para: {self.historico[-1]}')
        else:
            print('\nNão há paginas anteriores para voltar.')

    def mostrar_historico(self):
        if self.historico:
            print('\nHistórico de navegação:')
            for pagina in reversed(self.historico): #mostra o histórico do mais recente para o mais antigo
                print(pagina)
        else:
            print('\nNenhuma página visitada ainda.')

    def limpar_historico(self):
        self.historico.clear()
        print('\nHistórico de navegação foi apagado.')

#testar o navegador:
navegador = Navegador()

navegador.acessar_pagina('google.com')
navegador.acessar_pagina('github.com')
navegador.acessar_pagina('amazon.com')

navegador.mostrar_historico()

navegador.voltar_pagina() #voltando a página, apaga a última acessada

navegador.mostrar_historico()
navegador.limpar_historico()
navegador.mostrar_historico()