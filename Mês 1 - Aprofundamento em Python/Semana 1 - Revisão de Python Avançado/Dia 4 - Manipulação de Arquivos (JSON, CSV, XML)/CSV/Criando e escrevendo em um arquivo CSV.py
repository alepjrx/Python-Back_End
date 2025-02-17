import csv

#criando os dados para escrever no CSV:
dados = [
    ['nome', 'idade', 'cidade'],
    ['Lucas', 27, 'São Paulo'],
    ['Mariana', 22, 'Belo Horizonte'],
    ['Rafael', 35, 'Porto Alegre']
]

#criando um arquivo CSV e escrevendo os dados
with open('novo_dados.csv', 'w', encoding='utf-8', newline='') as arquivo:
    escritor_csv = csv.writer(arquivo)

    escritor_csv.writerows(dados) #escreve as linhas

print('Arquivo CSV criado com Sucesso!')