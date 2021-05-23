# Soma impares multiplos de tres
#num = int(input('Você quer saber o somatorio dos numeros de 1 até: '))
soma = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        cont = cont + 1
        soma = soma + c
print('O somatório de todos os numeros impares é: {}'.format(soma))






