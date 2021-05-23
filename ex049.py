# Tabuada v.2.0
n = int(input('Insira um número para ver a sua tabuada: '))
s = 0
print('\033[034m---TABUADA DE {}---'.format(n))
for c in range(0, 9):
    s += 1
    print('{} * {} = {}'.format(n, s, s * n))
