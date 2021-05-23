num = cont = quant = maior = menor = soma = 0
resp = 'S'
while resp in 'Ss':
    num = int(input('Digite um número:'))
    quant += 1
    soma += num
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            menor = num
        elif num < menor:
            maior = num
    resp = str(input('Quer continuar? [S/N] '))
media = soma / quant
print('Você digitou {} numeros'.format(quant))
print('A média entre os numeros digitados é: {}'.format(media))
print('O maior numero digitado foi {} e o menor foi {}'.format(maior, menor))