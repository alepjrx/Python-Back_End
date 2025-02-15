'''
Abrindo e Fechando arquivos em Python

Em Python, usamos a função open() para abrir arquivos. Quando terminamos de trabalhar com um
arquivo, devemos fechá-lo para evitar problemas de memória e corrupção de dados.
'''

#Sintaxe básica de open()

'''variavel_arquivo = open('meuarquivo1.txt', 'modo')'''
#define como será chamado o arquivo, qual arquivo é e o modo de abertura do arquivo que define como será tratado
'''
Modos de abertura do arquivo:
 'r' - Leitura (read) - Abre o arquivo para leitura. O arquivo deve existir
 'w' - Escrita (write) - Cria um arquivo novo ou sobrescreve um arquivo já existente
 'a' - Adição (append) - Adiciona conteúdo ao final do arquivo. Se não existir, cria um novo.
 'r+' - Leitura e Escrita - Lê e escreve sem apagar o conteúdo original
 'w+' - Escrita e Leitura - Apaga o conteúdo existente e escreve um novo
 'a+' - Adição e Leitura - Lê o arquivo e adiciona conteúdo ao final
'''
#(Execução de todo processo do arquivo)

'''variavel_arquivo.close''' #dessa forma, após trabalhar com o arquivo você o fecha e impede a corrupção dos dados

'''
Exemplo de abertura e fechamento de um arquivo:
'''

variavel_arquivo = open('meuarquivo1.txt', 'r') #abriu e definiu como será tratado
print('Arquivo aberto.')

variavel_arquivo.close() #fechou o arquivo


'''
Exemplo de criação e abertura de um novo arquivo:
'''

arquivo1 = open('arquivo1.txt', 'w')
arquivo1.write('"Lorem ipsum dolor sit amet."\n')
arquivo1.close()

'''
Exemplo de como adicionar conteúdo a um arquivo já existente:
'''

arquivo2 = open('arquivo1.txt', 'a')
arquivo2.write('Ut enim ad minima veniam, quis nostrum exercitationem ullam corporis suscipit laboriosam, nisi ut aliquid ex ea commodi consequatur?')
arquivo2.close()

'''
Importância de fechar arquivos:
 - Perda de informações
 - Bloqueio do arquivo para abertura/leitura em outros programas
 - Consumo excessivo de memória
'''