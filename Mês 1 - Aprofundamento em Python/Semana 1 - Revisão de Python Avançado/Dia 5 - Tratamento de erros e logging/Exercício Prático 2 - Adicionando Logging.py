#Exercício Prático 2

'''
2 - Adicionando Logging
Altere seu código para:
 - Registrar os erros em um arquivo chamado "erros.log"
 - Usar logging.error() ao capturar exceções
 - Manter as mensagens de erro para o usuário
'''

import logging

#configurar o logging
logging.basicConfig(filename='erros.log', level=logging.ERROR, format='%asctime)s - %(levelname)s - %(message)s')

try:
    numero = input('Digite um número: ')
    numero = int(numero)
    resultado = 10 / numero
    print(f'Resultado: {resultado}')
except ValueError as erro:
    print('Erro: Você digitou um valor inválido.')
    logging.error(f'Erro de valor inválido: {erro}') #registra no log
except ZeroDivisionError as erro:
    print('Erro: Não é possível dividir por zero.')
    logging.error(f'Erro de divisão por zero: {erro}') #registra no log