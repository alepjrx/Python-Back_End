import json

dados = {"marca": "Toyota", "modelo": "Corolla", "Ano": 2022}

#convertendo dicionário para string JSON
json_string = json.dumps(dados, indent=2) #tranforma um dicionário em uma string JSON

print(json_string)