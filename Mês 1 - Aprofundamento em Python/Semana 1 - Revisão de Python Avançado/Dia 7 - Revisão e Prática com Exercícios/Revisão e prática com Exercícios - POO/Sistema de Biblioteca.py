class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.disponivel = True

    def exibir_detalhes(self):
        print(f'Título do Livro: {self.titulo}, autor: {self.autor}, disponibilidade: {self.disponivel}')

    def emprestar(self):
        if self.disponivel:
            self.disponivel = False #caso esteja disponível, transforma em "False", ou seja, indisponibiliza
            print(f'O livro {self.titulo} pode ser emprestado.')
        else:
            print(f'O livro {self.titulo} não está disponível.')

    def devolver(self):
        if not self.disponivel:
            self.disponivel = True
            print(f'O livro {self.titulo} foi devolvido.')
        else:
            print(f'O livro {self.titulo} não está emprestado.')

livro1 = Livro('A Divina Comédia', 'Dante Alighieri')
livro2 = Livro('V de Vingança', 'Alan Moore')
livro3 = Livro('Anjos e Demônios', 'Dan Brown')

livro1.exibir_detalhes()
livro1.emprestar()
livro1.exibir_detalhes()
livro1.emprestar()

livro2.exibir_detalhes()
livro2.emprestar()
livro2.exibir_detalhes()
livro2.emprestar()

livro3.exibir_detalhes()
livro3.emprestar()
livro3.devolver()