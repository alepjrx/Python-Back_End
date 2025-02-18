'''
Podemos gerar erros intencionalmente usando raise
'''

def verificar_idade(idade):
    if idade < 18:
        raise ValueError('Idade mínima é de 18 anos')
    return 'Acesso Permitido.'

print(verificar_idade(20)) #aqui vai passar
print(verificar_idade(15)) #aqui vai gerar um erro


'''
Por que usar raise?
 - Para validar entrada de dados e impedir valores inválidos antes que causem problemas
'''