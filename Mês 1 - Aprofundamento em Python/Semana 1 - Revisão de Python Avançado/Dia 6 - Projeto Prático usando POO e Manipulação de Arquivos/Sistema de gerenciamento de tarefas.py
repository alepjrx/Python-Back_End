'''
                                    Projeto: Sistema de Gerenciamento de Tarefas
 - O sistema poderá adicionar, listar e remover tarefas
 - As tarefas serão armazenadas em um arquivo tarefas.json
 - Vamos usar POO para estruturar o código
'''

'''
Estrutura do Projeto:
Teremos uma classe GerenciadorTarefas que fará:
 - Adicionar tarefas ao arquivo JSON
 - Listar tarefas salvas
 - Remover tarefas pelo nome
'''

import json #importamos o módulo json, que será usado para salvar e carregar as tarefas de um arquivo JSON

class GerenciadorTarefas: #criamos a classe GerenciadorTarefas para gerenciar a lista de tarefas
    def __init__(self, arquivo='tarefas.json'): #o método __init__ é chamado automaticamente ao criar um objeto dessa classe
        self.arquivo = arquivo #define o nome do arquivo onde as tarefas serão armazenadas
        self.tarefas = self.carregar_tarefas() #chama o método carregar_tarefas() para carregar as tarefas do arquivo JSON

    def carregar_tarefas(self): #aqui, tentamos abrir o arquivo JSON e carregar as tarefas
        try:
            with open(self.arquivo, 'r', encoding='utf-8') as f: #abre o arquivo JSON em modo de leitura ('r')
                return json.load(f) #converte os dados JSON em uma lista Python
        except FileNotFoundError:
            return [] #retorna uma lista vazia se o arquivo não existir
        except json.JSONDecodeError:
            return [] #retorna lista vazia caso o JSON esteja corrompido

    def salvar_tarefas(self):
        with open(self.arquivo, 'w', encoding='utf-8') as f: #abre o arquivo JSON em modo de escrita ('w')
            json.dump(self.tarefas, f, indent=4, ensure_ascii=False) #salva a lista de tarefas no arquivo, formatando com indentação para melhor leitura

    def adicionar_tarefa(self, descricao): #adiciona uma nova tarefa à lista e salva no arquivo JSON
        self.tarefas.append({'descricao': descricao, 'status': 'Pendente'})
        self.salvar_tarefas()
        print(f'Tarefa "{descricao}" adicionada com sucesso.')

    def listar_tarefas(self): #lista as tarefas salvas no arquivo JSON
        if not self.tarefas:
            print('\nNenhuma tarefa encontrada.')
            return
        else:
            print('Lista de Tarefas')
            for indice, tarefa in enumerate(self.tarefas, start=1):
                print(f'{indice}. {tarefa['descricao']} - {tarefa['status']}')

    def remover_tarefa(self, indice): #remove uma tarefa pelo índice informado
        try:
            tarefa_removida = self.tarefas.pop(indice - 1) #remove pelo indice (ajustado pois indexes começam em 0)
            self.salvar_tarefas()
            print(f'Tarefa "{tarefa_removida['descricao']}" removida com sucesso.')
        except IndexError:
            print('Erro: Índice inválido! Escolha um número válido.')

    def marcar_concluida(self, indice): #marcar uma tarefa como concluída
        try:
            self.tarefas[indice - 1]['status'] = 'concluída'
            self.salvar_tarefas()
            print(f'Tarefa "{self.tarefas[indice - 1]['descricao']}" marcada como concluída.')
        except IndexError:
            print('Erro: Índice Inválido! Escolha um número válido.')

def exibir_menu(): #exibe o menu interativo e permite interações do usuário
    gerenciador = GerenciadorTarefas()

    while True:
        print('\n=== Gerenciador de Tarefas ===\n')
        print('1. Adicionar Tarefa')
        print('2. Listar Tarefas')
        print('3. Remover Tarefa')
        print('4. Marcar Tarefa como Concluída')
        print('5. Sair do Programa')

        opcao = input('\nEscolha uma Opção: ')

        if opcao == '1':
            descricao = input('Digite a descrição da Tarefa: ')
            gerenciador.adicionar_tarefa(descricao)

        elif opcao == '2':
            gerenciador.listar_tarefas()

        elif opcao == '3':
            indice = int(input('Digite o número da tarefa para remover: '))
            gerenciador.remover_tarefa(indice)

        elif opcao == '4':
            indice = int(input('Digite o número da tarefa para marcar como concluída: '))
            gerenciador.marcar_concluida(indice)

        elif opcao == '5':
            print('Saindo do Programa...')
            break

        else:
            print('Opção Inválida. Tente novamente.')

exibir_menu()