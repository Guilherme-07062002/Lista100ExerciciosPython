num = 0
quant = 0
soma = 0
while num != 999:
    num = int(input('Digite um numero inteiro: '))
    if num != 999:
        quant += 1
        soma += num
print('Você digitou {} numeros.\nE a soma entre eles deu: {}'.format(quant,soma))
print('FIM')