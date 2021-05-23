soma = 0
maioridadehomem = 0
nomevelho = ''
totmulher20 = 0
for p in range(1, 5):
    print('------ {}° PESSOA ------'.format(p))
    nome = str(input('Insira o nome da {}° pessoa: '.format(p))).strip()
    idade = int(input('Insira sua idade: '))
    sexo = str(input('Sexo[M,F]: ')).strip()
    soma += idade
    if p == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if idade > maioridadehomem and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1
print('A média da idade das 2 pessoas é:{}'.format(soma / 2))
print('O homem mais velho tem {} anos e seu nome é {}'.format(maioridadehomem, nomevelho))
print('O número de mulheres com menos de 20 anos é:{}'.format(totmulher20))
