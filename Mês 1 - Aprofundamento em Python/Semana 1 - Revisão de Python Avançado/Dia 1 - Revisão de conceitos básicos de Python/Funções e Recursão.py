def soma(a, b):
    return a + b

resultado = soma(4, 3)
print(f'A soma de 4 + 3 é {resultado}')

print('\n---\n')

def multiplicar(a, b):
    return a * b

resultado = multiplicar(3,5)
print(f'3 multiplicado por 5 é {resultado}')


#ctrl-c ctrl-v - linha 17:24
def soma_numeros(n):
    if n == 1:  # Caso base: se n for 1, retorna 1
        return 1
    else:  # Passo recursivo: soma n com a soma dos números até n-1
        return n + soma_numeros(n - 1)

resultado = soma_numeros(5)
print(f'A soma dos números de 1 até 5 é {resultado}')