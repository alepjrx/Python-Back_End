'''
As Hash Tables (ou dicionários) mapeiam chaves para valores e usam funções hash para eficiência.
'''

class HashTable:
    def __init__(self, size =10):
        self.size = size
        self.table = [[] for _ in range(size)]

    def _hash(self, key): #funções hash simples
        return hash(key) % self.size

    def insert(self, key, value): #insere um par chave-valor
        index = self._hash(key)
        for pair in self.table[index]:
            if pair[0] == key:
                pair[1] = value
                return
        self.table[index].append([key, value])

    def get(self, key): #obtém um valor pela chave
        index = self._hash(key)
        for pair in self.table[index]:
            if pair[0] == key:
                return pair[1]
        return None

    def remove (self, key): #remove um par chave-valor
        index = self._hash(key)
        self.table[index] = [pair for pair in self.table[index] if pair[0] != key]

    def display(self): #mostra a tabela hash
        for i, bucket in enumerate(self.table):
            print(f'{i}: {bucket}')

#testando a tabela hash
ht = HashTable()
ht.insert('nome', 'Alice')
ht.insert('idade', 25)
print(ht.get('nome')) #deve imprimir Alice
ht.remove('idade')
ht.display()