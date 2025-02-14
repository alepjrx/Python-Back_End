'''
1 - Criar uma classe [Produto] com atributos privados [_nome] [_preco] e um método [exibir_detalhes()]

2 - Crie métodos [set_preco(novo_preco)] e [get_preco()] para modificar e acessar [_preco]

3 - Teste criando objetos e modificando os valores com métodos apropriados
'''

class Produto:
    def __init__(self, nome, preco):
        self._nome = nome
        self._preco = preco

    def exibir_detalhes(self):
        print(f'Produto: {self._nome} | Preço: {self._preco:.2f}')

    def get_preco(self): #método getter para acessar o preço
        return self._preco

    def set_preco(self, novo_preco): #método setter para modificar o preço (com validação)
        if novo_preco > 0:
            self._preco = novo_preco
            print(f'Novo preço definido: R${self._preco:.2f}')
        else:
            print('Erro: O preço deve ser um valor positivo.')


#criando objetos da classe "Produto"
produto1 = Produto('Celular', 1500)
produto2 = Produto('Notebook', 2500)
produto3 = Produto('Fone de Ouvido', 400)

#para exibir detalhes dos produtos
produto1.exibir_detalhes()
produto2.exibir_detalhes()
produto3.exibir_detalhes()

#para modificar o preço com set_preco()
produto1.set_preco(1800) #define o novo valor

#para obter o preço com get_preco()
preco_atual = produto1.get_preco()
print(f'Preço atualizado: R${preco_atual:.2f}')