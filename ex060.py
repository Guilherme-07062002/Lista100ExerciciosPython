num = int(input('Digite um número para saber seu fatorial: '))
cont = num
res = num
total = 1
print('{}!'.format(num))
for c in range(1, num + 1):
    if cont >= 1:
        total = res * total
        print('{}'.format(cont), end=' ')
        cont -= 1
        res = cont * res
        res = cont

print('= {}'.format(total))