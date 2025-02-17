import csv

with open('dados.csv', 'r', encoding='utf-8') as arquivo:
    leitor_csv = csv.DictReader(arquivo)

    for linha in leitor_csv:
        print(linha)