#Exercício Prático 4

'''
2 - Criando um sistema de Login com Logging
Crie um sistema de login que
 - Peça um nome e senha
 - Verifique se os dados são corretos (usuário = 'admin', senha = '1234')
 - Se errar 3 vezes, levante um exception e registre no logging
 - Cada tentativa errada deve ser registrada no log
'''

import logging

#configurando logging
logging.basicConfig(filename='erros.log', level=logging.WARNING, format='%(asctime)s - %(levelname)s - %(message)s')

#credenciais corretas
usuario_correto = 'admin'
senha_correta = '1234'
tentativas = 0

while tentativas < 3:
    try:
        usuario = input('Usuario: ')
        senha = input('Senha: ')

        if usuario == usuario_correto and senha == senha_correta:
            print('Login Bem-Sucedido.')
            break
        else:
            tentativas += 1
            raise ValueError('Usuário ou Senha incorretos.')

    except ValueError as erro:
        print(f'Erro: {erro} ({tentativas}/3)')
        logging.warning(f'Tentativa de Login inválida: {erro}')

#se errar 3 vezes, levanta um erro
if tentativas == 3:
    logging.error('Usuário bloqueado após 3 tentativas.')
    raise Exception('Muitas tentativas inválidas. Acesso Bloqueado.')