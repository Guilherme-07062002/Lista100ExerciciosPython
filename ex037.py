# Conversor de bases númericas

num = int(input('Digite um numero para conversão: '))
conv = int(input('''Escolha qual base para conversão: 
1 - Binário
2 - Octal
3 - Hexadecimal
Digite aqui: '''))

if conv == 1:
    print('{} convertido para binário é: {}'.format(num, bin(num)[2:]))
elif conv == 2:
    print('{} convertido para octal é: {}'.format(num, oct(num)[2:]))
elif conv == 3:
    print('{} convertido para hexadecimal é: {}'.format(num, hex(num)[2:]))
else:
    print('Opção inválida, tente novamente.')
