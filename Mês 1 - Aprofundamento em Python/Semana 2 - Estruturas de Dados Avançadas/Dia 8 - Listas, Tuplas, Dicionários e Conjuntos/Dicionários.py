'''
Dicionários
 Dicionários armazenam pares de chave-valor, sendo úteis para representar dados estruturados
'''

#criando o dicionário
pessoa = {
    'nome': 'Carlos',
    'idade': '30',
    'cidade': 'São Paulo'
}

#acessando os valores
print(pessoa['nome'])
print(pessoa.get('idade'))

#manipulando os valores
pessoa['profissão'] = 'Engenheiro' #assim adiciona um valor
del pessoa['cidade'] #assim exclui o valor