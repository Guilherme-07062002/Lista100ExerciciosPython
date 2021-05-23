# Criando menu de opções
num1 = int(input('Insira o primeiro valor: '))
num2 = int(input('Insira o segundo valor: '))
anunciado = '''-----SELECIONE-----
[1]Somar
[2]Multiplicar
[3]Maior
[4]Novos numeros
[5]Sair do programa
>>>> '''
resposta = int(input(anunciado))

while resposta != 5:
    if resposta == 1:
        print('O resultado da soma é: \033[34m{}\033[m\n'.format(num1+num2))
        resposta = int(input(anunciado))
    if resposta == 2:
        print('O resultado da multiplicação é: \033[34m{}\033[m\n'.format(num1*num2))
        resposta = int(input(anunciado))
    if resposta == 3:
        if num1 > num2:
            print('O número \033[34m{}\033[m é maior.\n'.format(num1))
            resposta = int(input(anunciado))
        elif num2 > num1:
            print('O numero \033[34m{}\033[m é maior\n'.format(num2))
            resposta = int(input(anunciado))
        elif num2 == num1:
            print('\033[33mOs numeros são iguais\033[m\n')
            resposta = int(input(anunciado))
    if resposta == 4:
        num1 = int(input('Digite novo valor do primeiro número: '))
        num2 = int(input('Digite novo valor do segundo número: '))
        resposta = int(input(anunciado))
print('\033[31m-----FIM DA OPERAÇÃO-----')