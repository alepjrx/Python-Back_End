with open ('documento1.txt', 'r') as doc: #define que o documento vai ser puxado por modo de leitura ('r') e chamado de "doc"
    conteudo = doc.read() #lê o conteúdo do documento "doc"
    print(conteudo) #imprime o conteúdo do documento "doc" no console

with open ('documento2.txt', 'w') as doc: #cria o documento e define que o documento vai ser puxado em modo de escrita ('w')
    doc.write('Linha adicionada por meio de .write - 1')
    doc.write('\nLinha adicionada por meio de .write - 2')

with open ('documento2.txt', 'a') as doc: #adiciona uma linha ao final do documento sem apagar as existentes por meio de ('a')
    doc.write('\nLinha adicionada por meio de .write - 3')

with open ('documento2.txt', 'r') as doc:
    conteudo = doc.read()
    print(conteudo)

print('\n---\n')

with open ('notas.txt', 'r') as notas_alunos:
    notas = notas_alunos.read()
    print(notas)