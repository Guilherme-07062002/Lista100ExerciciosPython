# Analisando triangulo v1.0
n1 = float(input('Digite o comprimento da primeira reta: '))
n2 = float(input('Digite o comprimento da segunda reta: '))
n3 = float(input('Digite o comprimento da terceira reta: '))
soma1 = n1 + n2
soma2 = n1 + n3
soma3 = n2 + n3
if n1 < soma3 and n2 < soma2 and n3 < soma1:
    print('Pode formar um triangulo.')
else:
    print('Não é possivel formar um triangulo.')