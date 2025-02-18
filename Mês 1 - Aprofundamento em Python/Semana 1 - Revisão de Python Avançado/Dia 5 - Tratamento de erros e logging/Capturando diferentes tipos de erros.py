'''
Podemos capturar vários tipos de exceções de maneira mais específica:
'''

try:
    lista = [1, 2, 3]
    print(lista[5]) #aqui, induzimos o erro para acessar um index inválido
except IndexError as erro:
    print(f'Erro de Índice: {erro}')
except Exception as erro:
    print(f'Erro Genérico: {erro}')

'''
Explicação:
 - O erro IndexError acontece pois o index 5 não existre na lista
 - O programa captura o erro e o exibe sem travar
 - O Exception captura qualquer outro erro não tratado anteriormente
'''