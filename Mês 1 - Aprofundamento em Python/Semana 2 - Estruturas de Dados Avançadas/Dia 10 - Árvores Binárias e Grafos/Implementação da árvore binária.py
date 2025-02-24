'''
Implementação da Árvore Binária

Começaremos implementando uma árvore binária simples em Python. Vamos criar uma classe Node
para representar os nós da árvore e uma classe BinaryTree para a árvore em si.

Estrutura da classe:
1 - Classe Node - Representa cada nó da árvore. Cada nó terá um valor e referências para
o filho esquerdo e o filho direito.
2 - Classe BinaryTree - Representa a árvore binária. Terá métodos para inserir elementos e
percorrer a árvore.
'''

class Node:
    def __init__(self, value):
        self.value = value #valor do nó
        self.left = None #filho esquerda
        self.right = None #filho direita

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self._insert_recursive(node.left, value)
        else:
            if node.right is None:
                node.right = Node(value)
            else:
                self._insert_recursive(node.right, value)

    def inorder_traversal(self, node):
        if node:
            self.inorder_traversal(node.left)
            print(node.value, end=' ')
            self.inorder_traversal(node.right)

#exemplo de uso:

tree = BinaryTree()

tree.insert(10)
tree.insert(7)
tree.insert(9)
tree.insert(2)

#percorrendo a árvore em ordem
tree.inorder_traversal(tree.root)

'''
Explicação:
 - A função insert insere um valor na árvore, respeitando as regras de uma árvore binária de busca.
 - A função inorder_traversal percorre a árvore de forma recursiva, visitando primeiro o filho esquerdo,
depois o nó e finalmente o filho direito (ordem crescente de valores)
'''