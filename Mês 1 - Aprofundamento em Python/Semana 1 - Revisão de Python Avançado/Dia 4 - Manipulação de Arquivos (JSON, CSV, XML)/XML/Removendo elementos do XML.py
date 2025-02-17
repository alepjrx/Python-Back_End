import xml.etree.ElementTree as et

#carregar o XML
arvore = et.parse('dados.xml')
raiz = arvore.getroot()

#remover um usuário (Carlos)
for usuario in raiz.findall('usuario'):
    if usuario.find('nome').text == 'Carlos':
        raiz.remove(usuario)

#salvar o XML atualizado
arvore.write('dados_sem_carlos.xml', encoding='utf-8', xml_declaration=True)

print('Usuário "Carlos" removido com sucesso de "dados.xml" e criado "dados_sem_carlos.xml')

'''
Explicação:
 - Buscamos o usuário "Carlos"
 - Removemos ele com raiz.remove(usuario)
 - Salvamos nosso arquivo
'''