import json

#criando um dicionário Python:

dados = {
    "nome": "Carlos",
    "idade": 28,
    "cidade": "Curitiba",
    "habilidades": ["Django", "Javascript"]
}

with open('novo_dados.json', 'w', encoding='utf-8') as arquivo:
    json.dump(dados, arquivo, indent=4, ensure_ascii=False)

print('Arquivo JSON criado com sucesso!')

'''
Explicação:
 json.dump(dados, arquivo) - Salva o dicionário em um arquivo JSON
 indent=4 - Formata o JSON para ficar legível
 ensure_ascii=False - Permite caracteres especiais (como acentos)
'''