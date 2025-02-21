class Produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    def exibir_detalhes(self):
        print(f'\nNome: {self.nome}, preço: {self.preco}, quantidade em estoque: {self.quantidade}.')

    def adicionar_estoque(self, valor):
        self.quantidade += valor

    def remover_estoque(self, valor):
        self.quantidade -= valor

produto_notebook = Produto('Notebook', 2500.00, 4)
produto_celular = Produto('iPhone', 4000.00, 5)
produto_videogame = Produto('PlayStation 5', 4100.00, 2)

produto_videogame.exibir_detalhes()
produto_videogame.adicionar_estoque(2)
produto_videogame.exibir_detalhes()

produto_celular.exibir_detalhes()
produto_celular.remover_estoque(3)
produto_celular.exibir_detalhes()

produto_notebook.exibir_detalhes()
produto_notebook.adicionar_estoque(2)
produto_notebook.exibir_detalhes()

