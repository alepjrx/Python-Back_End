produto = {
    'nome': 'Camiseta',
    'preço': 50,
    'tamanho': 'M',
}

print(produto['nome'], produto['tamanho'], produto['preço'])

produto['preço'] = 45 #modifica a chave "preço"
produto['estoque'] = 100 #adicionei uma chave nova chamada "estoque"
del produto['tamanho'] #excluí a chave "tamanho"

print(produto)