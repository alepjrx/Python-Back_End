import csv

with open('dados.csv', 'r', encoding='utf-8') as arquivo:
    leitor_csv = csv.reader(arquivo) #lê o CSV e retorna cada linha como uma lista

    for linha in leitor_csv:
        print(linha)