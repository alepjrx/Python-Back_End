'''
Podemos registrar logs em arquivos em vez de exibi-los no console
'''
import logging

logging.basicConfig(filename='app.log', level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')

try:
    resultado = 10 / 0
except ZeroDivisionError as erro:
    logging.error(f'Erro Ocorrido: {erro}')

'''
Explicação:
 - Se um erro ocorrer, ele será salvo no arquivo "app.log"
 - Isso ajuda a monitorar problemas sem exibir erros diretamente no sistema
'''