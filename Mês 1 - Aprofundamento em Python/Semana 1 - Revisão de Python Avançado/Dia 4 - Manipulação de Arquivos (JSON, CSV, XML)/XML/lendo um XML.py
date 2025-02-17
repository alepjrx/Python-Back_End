import xml.etree.ElementTree as et

#carregar o arquivo XML
arvore = et.parse('dados.xml')
raiz = arvore.getroot()

#percorrendo os elementos:
for usuario in raiz.findall('usuario'):
    nome = usuario.find('nome').text
    idade = usuario.find('idade').text
    cidade = usuario.find('cidade').text

    print(f'Nome: {nome}, Idade: {idade}, Cidade: {cidade}')

'''
Explicação:
 ET.parse('dados.xml') - Carrega o arquivo .xml
 getroot() - Obtém o elemento raiz <usuarios>
 findall('usuario') - Encontra todos os elementos <usuario>
 find('nome').text - Obtém o texto dentro da tag <nome>
'''