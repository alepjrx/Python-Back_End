'''
Percursos em Grafos: DFS e BFS

Os percursos em grafos são usados para visitar os nós de um grafo de forma eficiente.
'''

'''
Busca em profundidade (DFS - Depth First Search)
O DFS explora um caminho o máximo possível antes de voltar e explorar outros.
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

    def dfs(self, node, visited=None):
        if visited is None:
            visited = set()
        if node not in visited:
            print(node, end=' ')
            visited.add(node)
            for neighbor in self.graph[node]:
                self.dfs(neighbor, visited)

#criando o grafo e testando o DFS
g = Graph()
g.add_edge(1, 2)
g.add_edge(1, 3)
g.add_edge(2, 4)
g.add_edge(3, 5)

print('DFS Traversal: ')
g.dfs(1) #imprimir um caminho válido começando do nó 1



'''
Busca em Largura (BFS - Breadth First Search)
O BFS explora todos os vizinhos de um nó antes de explorar os vizinhos dos vizinhos
'''

from collections import deque

class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        self.graph[u].append(v)
        self.graph[v].append(u) #para grafo não direcionado

    def bfs(self, start):
        visited = set()
        queue = deque([start])
        visited.add(start)

        while queue:
            node = queue.popleft()
            print(node, end=' ')
            for neighbor in self.graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)
                    visited.add(neighbor)

#criando o grafo e testando BFS
g = Graph()
g.add_edge(1, 2)
g.add_edge(1, 3)
g.add_edge(2, 4)
g.add_edge(3, 5)

print('\nBFS Traversal: ')
g.bfs(1) #imprime um caminho válido em BFS


'''
Comparação entre DFS e BFS:
 DFS - Melhor para explorar profundamente um caminho antes de tentar outro. Pode ser implementado
com recursão ou pilha.
 BFS - Melhor para encontrar o caminho mais curto em um grafo não ponderado. Utiliza Fila
'''