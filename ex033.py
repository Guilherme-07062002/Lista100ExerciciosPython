# Maior e menor valores

n1 = int(input('Digite o primeiro numero:'))
n2 = int(input('Digite o segundo numero:'))
n3 = int(input('Digite o terceiro numero:'))
# Verificando o menor
if n1 > n2 and n1 > n3:
    print('O maior é: {}'.format(n1))
elif n2 > n1 and n2 > n3:
    print('O maior é: {}'.format(n2))
else:
    print('O maior é {}'.format(n3))
# Verificando o maior
if n1 < n2 and n1 < n3:
    print('O menor é: {}'.format(n1))
elif n2 < n1 and n2 < n3:
    print('O menor é: {}'.format(n2))
else:
    print('O menor é {}'.format(n3))
