import xml.etree.ElementTree as ET

#carregar o arquivo XML
arvore = ET.parse('dados.xml')
raiz = arvore.getroot()

#percorrendo os elementos:
for usuario in raiz.findall('usuario'):
    nome = usuario.find('nome').text
    idade = usuario.find('idade').text
    cidade = usuario.find('cidade').text

    print(f'Nome: {nome}, Idade: {idade}, Cidade: {cidade}')