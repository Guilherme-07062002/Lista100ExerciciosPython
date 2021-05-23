# Soma dos pares
soma = 0
cont = 0
for c in range(1, 7):
    n = int(input('Digite o {}° numero: '.format(c)))
    if n % 2 == 0:
        soma += n
        cont += 1
if soma > 0:
    print('O somatório dos valores é: {}'.format(soma))
else:
    print('Tente novamento inserindo numeros pares.')