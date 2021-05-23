num = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))
c = 1
while c <= 10:
    print('{} -'.format(num), end=' ')
    num += razao
    c += 1
print('FIM')
