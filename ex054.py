# Grupo da maioridade
from datetime import date
anoatual = date.today().year
demaior = 0
demenor = 0

for c in range(0, 7):
    anonasc = int(input('Digite o ano de nascimento da {}° pessoa: '.format(c + 1)))
    if anoatual - anonasc >= 18:
        demaior += 1
    else:
        demenor += 1
print('\n')
if demaior > 0 and demenor > 0:
    print('''O numero de pessoas maiores : {}
Não maiores: {}'''.format(demaior, demenor))
elif demaior > 0 and demenor == 0:
    print('''Não tem pessoas menores.
O número de maiores é: {}'''.format(demaior))
elif demenor > 0 and demaior == 0:
    print('''Não tem pessoas maiores.
O número de menores é: {}'''.format(demenor))
