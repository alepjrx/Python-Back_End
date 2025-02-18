#Exercício Prático 3

'''
2 - Validação de nome com tratamento de erros
Crie um programa que:
 - Peça um nome ao usuário
 - Verifique se o espaço de nome não está vazio
 - Se estiver vazio, levante um erro com raise ValueError
 - Trate o erro e registre no logging
'''

import logging

#configurar o logging
logging.basicConfig(filename='erros.log', level=logging.ERROR, format='%(asctime)s - %(levelname)s - %message)s')

try:
    nome = input('Digite seu nome: ').strip()

    #se o nome estiver vazio, levanta um erro:
    if not nome:
        raise ValueError('Nome não pode estar vazio.')

    print(f'Bem vindo, {nome}.')
except ValueError as erro:
    print('Erro: Nome inválido.')
    logging.error(f'Erro de nome inválido: {erro}') #registra no log