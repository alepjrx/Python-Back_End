import csv

#lista de dicionários
dados = [
    {'nome': 'Bruno', 'idade': 29, 'cidade': 'Brasília'},
    {'nome': 'Fernanda', 'idade': 33, 'cidade': 'Recife'},
    {'nome': 'Paula', 'idade': 26, 'cidade': 'Florianópolis'}
]

#criando e escrevendo em um arquivo CSV:
with open('pessoas.csv', 'w', encoding='utf-8', newline='') as arquivo:
    colunas = ['nome', 'idade', 'cidade']
    escritor_csv = csv.DictWriter(arquivo, fieldnames=colunas)

    escritor_csv.writeheader() #escreve o cabeçalho
    escritor_csv.writerows(dados) #escreve o corpo que serão os dados

print('Arquivo CSV criado com Sucesso!')