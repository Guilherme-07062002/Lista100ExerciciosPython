# Progressão aritmetica
num = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))
s = 0
print(num)
n = num
for c in range(0, 9):
    n += razao
    print(n, end='-')
print('FIM')

print('\nEssa é uma PA onde o primeiro elemento é {} e a razão é {}'.format(num, razao))