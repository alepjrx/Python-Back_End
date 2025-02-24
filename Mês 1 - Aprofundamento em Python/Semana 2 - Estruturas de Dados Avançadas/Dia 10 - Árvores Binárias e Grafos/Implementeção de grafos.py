'''
Implementação de Grafos

Vamos criar uma representação simples de um grafo usando lista de adjacência.

Estrutura da classe:
1 - Classe Graph - Representa o grafo. Terá métodos para adicionar arestas e imprimir o grafo.
'''

class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        self.graph[u].append(v)
        self.graph[v].append(u) #para um grafo não direcionado

    def print_graph(self):
        for node in self.graph:
            print(f'{node}: {self.graph[node]}')

#exemplo de uso:
g = Graph()
g.add_edge(1, 2)
g.add_edge(1, 3)
g.add_edge(2, 4)


#imprimindo o grafo
g.print_graph()