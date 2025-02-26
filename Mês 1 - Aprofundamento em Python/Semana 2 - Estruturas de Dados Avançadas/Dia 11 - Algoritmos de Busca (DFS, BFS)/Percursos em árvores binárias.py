'''
Percursos em árvores binárias

Os percursos determinam a ordem em que os nós das árvores são visitados:

 - Pré-ordem (preorder): Visita o nó atual antes dos filhos (raiz -> esquerda -> direita)
 - Em ordem (inorder): Visita a subárvore esquerda, depois o nó atual, depois a direita. (esquerda -> raiz -> direita)
 - Pós-ordem (postorder): Visita os filhos antes do nó atual (esquerda -> direita -> raiz)
'''

#implementando esses percursos:

class Node:
    def __init__(self, value):
        self.value = value #valor do nó
        self.left = None #filho à esquerda
        self.right = None #filho à direita

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
                self._insert_recursive(self.root, value)

    def inorder(self, node):
        if node:
            self.inorder(node.left)
            print(node.value, end=' ')
            self.inorder(node.right)

    def preorder(self, node):
        if node:
            print(node.value, end=' ')
            self.preorder(node.left)
            self.preorder(node.right)

    def postorder(self, node):
        if node:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.value, end=' ')

#criando a árvore e testando os percursos:
tree = BinaryTree()
tree.insert(10)
tree.insert(13)
tree.insert(6)
tree.insert(2)
tree.insert(8)
tree.insert(1)

print('\nInorder traversal: ')
tree.inorder(tree.root)

print('\nPreorder traversal: ')
tree.preorder(tree.root)

print('\nPostorder traversal: ')
tree.postorder(tree.root)