'''
O módulo logging permite registrar mensagens de erro, depuração e informações do sistema
'''

#configuração básica do logging

import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

logging.info('Este é um aviso informativo!')
logging.warning('Atenção! Algo pode estar errado.')
logging.error('Erro detectado!')

'''
Níveis de log:
 DEBUG - Mensagens para Depuração
 INFO - INformações gerais do sistema
 WARNING - Avisos sobre possíveis problemas
 ERROR - Erros que precisam ser corrigidos
 CRITICAL - Erros graves que impedem o funcionamento do sistema
'''