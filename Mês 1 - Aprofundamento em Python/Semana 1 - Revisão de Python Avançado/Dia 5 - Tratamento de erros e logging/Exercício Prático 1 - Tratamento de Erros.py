#Exercício Prático 1

'''
1 - Tratamento de Erros ao converter e dividir valores:
Crie um programa que:
 - Solicite um número ao usuário
 - Tente converter para int
 - Tente dividir 10 pelo número digitado
 - Trate erros como: Número Inválido e Divisão por Zero
'''

try:
    numero = input('Digite um Número: ')
    numero = int(numero)
    resultado = 10 / numero
    print(f'Resultado: {resultado}')
except ValueError:
    print('Erro: Você digitou um valor inválido.')
except ZeroDivisionError:
    print('Erro: Não é possível dividir por Zero.')

