import xml.etree.ElementTree as et

#criando o elemento raiz
usuarios = et.Element('usuarios')

#adicionando um usuário
usuario1 = et.SubElement(usuarios, 'usuario')
et.SubElement(usuario1, 'nome').text = 'Mariana'
et.SubElement(usuario1, 'idade').text = '22'
et.SubElement(usuario1, 'cidade').text = 'Salvador'

#criando um novo arquivo XML
arvore = et.ElementTree(usuarios)
arvore.write('novo_usuarios.xml', encoding='utf-8', xml_declaration=True)
print('Arquivo XML "novo_usuarios" criado com sucesso!')