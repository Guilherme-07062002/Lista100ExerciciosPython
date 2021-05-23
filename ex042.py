# Analisando triangulo v2.0
n1 = float(input('Digite o comprimento da primeira reta: '))
n2 = float(input('Digite o comprimento da segunda reta: '))
n3 = float(input('Digite o comprimento da terceira reta: '))
soma1 = n1 + n2
soma2 = n1 + n3
soma3 = n2 + n3
if n1 < soma3 and n2 < soma2 and n3 < soma1 and n1 == n2 and n2 == n3:
    print('Pode formar um triangulo {}EQUILATERO{}'.format('\033[34m', '\033[m'))
elif n1 < soma3 and n2 < soma2 and n3 < soma1 and n1 == n2 or n2 == n3:
    print('Pode formar um triangulo {}ISÓSCELES{}'.format('\033[34m', '\033[m'))
elif n1 < soma3 and n2 < soma2 and n3 < soma1 and n1 != n2 and n2 != n3:
    print('Pode formar um triangulo {}ESCALENO{}'.format('\033[34m', '\033[m'))
else:
    print('Não é possivel formar um triangulo.')
