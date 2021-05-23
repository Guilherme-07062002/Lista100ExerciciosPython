# Numero por extenso
contagem = ('zero','um','dois','tres', 'quatro', 'cinco',
            'seis', 'sete', 'oito', 'nove', 'dez','onze', 'doze'
            'treze', 'catorze','quinze', 'dezesseis','dezessete',
            'dezoito', 'dezenove','vinte')
while True:
    num = int(input('Digite um numero entre 0 e 20: '))
    if 0 <= num <= 20:
        break
    print('Tente novamente: ',end=' ')
print(f'Você digitou o numero {contagem[num]}')