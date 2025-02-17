import xml.etree.ElementTree as et

#carregar o XML existente
arvore = et.parse('dados.xml')
raiz = arvore.getroot()

#modificar um elemento (alterar a idade de Ana)
for usuario in raiz.findall('usuario'):
    nome = usuario.find('nome').text
    if nome == 'Ana':
        usuario.find('idade').text = '26'

#salvar as alterações no arquivo
arvore.write('dados_modificado.xml', encoding='utf-8', xml_declaration=True)

print('Arquivo XML "dados.xml" atualizado com sucesso!')

'''
Explicação:
 - Lemos o arquivo "dados.xml" e localizamos a Ana
 - Alteramos a idade da Ana de 25 para 26
 - Salvamos as mudanças no arquivo "dados_modificado.xml"
'''