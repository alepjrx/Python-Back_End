import json

json_texto = '{"produto": "Notebook", "preco": 3500, "estoque": 10}'

#converter string JSON para dicionário
dados = json.loads(json_texto)

print(dados)
print(dados["produto"]) #acessa um item específico do JSON convertido