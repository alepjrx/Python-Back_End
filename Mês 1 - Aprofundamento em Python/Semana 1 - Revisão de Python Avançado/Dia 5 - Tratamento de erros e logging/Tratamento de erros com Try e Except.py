'''
Em Python, erros podem ser tratados com a estrutura try e except. Isso impede que o programa
pare abruptamente quando ocorre um erro.
'''

#Tratamento Básico:

try:
    numero = int(input('Digite um número: '))
    resultado = 10 / numero
    print(f'Resultado: {resultado}')
except ZeroDivisionError:
    print('Erro: Não é possível dividir por Zero!')
except ValueError:
    print('Erro: Você precisa digitar um número válido.')

'''
Explicação:
 - O código dentro de try é executado.
 - Se houver um erro, o programa busca um excpet compatível com o erro para tratá-lo
 - Aqui, lidamos com divisao por zero e erro ao converter um número
'''