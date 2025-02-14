numero = int(input('Digite um número: '))

for x in range(1, 11):
    print(f'{numero} x {x} = {numero * x}')

'''
Explicação do que acontece:

    Quando o número que o usuário adicionou entra no sistema, ele é calculado pela primeira vez
e então, exibido no console na estrutura do print (linha 4), após isso, o for loop executa
ele de novo porém aumentando o número pelo qual ele vai ser multiplicado em 1, por isso, 
o range(1,11) pois ele vai aumentando em 1 até chegar em 10.
    (O último número sempre é ignorado, por exemplo: se estiver até 10, ele só multiplica até
o 9. Os motivos devem ser os mesmos de index sempre começar em [0].)
'''