'''Estrutura básica de tratamento de exceções:'''

#ctrl-c ctrl-v - linha 5:24
'''
try:
    # Bloco de código onde o erro pode ocorrer
    numero = int(input("Digite um número: "))
    resultado = 10 / numero
    print(f"O resultado da divisão é: {resultado}")
except ZeroDivisionError:
    # Bloco de código que será executado se ocorrer um erro de divisão por zero
    print("Erro: Não é possível dividir por zero.")
except ValueError:
    # Bloco de código que será executado se ocorrer um erro de conversão de valor
    print("Erro: Você deve digitar um número válido.")
except Exception as e:
    # Bloco genérico para outros tipos de erros
    print(f"Erro inesperado: {e}")
else:
    # Bloco de código que será executado se não houver exceção
    print("Operação realizada com sucesso!")
finally:
    # Bloco de código que será executado sempre, independentemente de erro
    print("Fim da execução.")
'''

try:
    numero_1 = int(input('Digite um número: '))
    numero_2 = int(input('Digite outro número: '))

    resultado_div = numero_1 / numero_2
    print(f'O resultado da divisão de {numero_1} por {numero_2} é {resultado_div:.2f}')

except ValueError: #SE acontecer um erro de valor, como entrar um texto, irá realizar essa parte
    print('Erro: Você deve digitar apenas números.')

except ZeroDivisionError: #Caso um dos números entrados seja Zero, irá realizar essa parte
    print('Erro: Não é possível dividir por zero.')

except Exception as e: #Se for um erro inesperado, realiza essa parte
    print(f'Erro inesperado: {e}')

else: #Caso não haja nenhum erro, irá imprimir essa mensagem
    print('Divisão realizada com sucesso.')

finally: #Independente do resultado ou erro, irá imprimir essa mensagem ao final
    print('Fim da execução.')