import json

with open('dados.json', 'r', encoding='utf-8') as arquivo_json:
    dados = json.load(arquivo_json) #convertendo JSON para um dicionário

print(dados) #exibe o conteúdo como um dicionário Python

print(dados['nome']) #exibe apenas o valor solicitado