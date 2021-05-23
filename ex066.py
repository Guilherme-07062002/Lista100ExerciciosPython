# Varios numeros com flag
num = quant = soma = 0
while True:
    num = int(input('Digite um número(999 pra parar): '))
    if num == 999:
        break
    soma += num
    quant += 1
print(f'''Você digitou {quant} números.
A soma entre eles é: {soma}''')