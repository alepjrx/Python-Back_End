'''
O bloco Finally sempre será executado, independente de ocorrer um erro ou não.
'''

try:
    arquivo = open('dados.txt', 'r')
    conteudo = arquivo.read()
except FileNotFoundError:
    print('Erro: Arquivo não encontrado')
finally:
    print('Finalizando operação...')

'''
Uso do Finally:
 - Ideal para fechar arquivos, conexões do banco de dados, ou liberar recursos
'''