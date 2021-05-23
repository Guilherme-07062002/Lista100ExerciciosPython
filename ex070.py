# Estatisticas em produtos
total = maisdemil = menorpreco = cont = 0
nome = nomemaisbarato = preco = escolha = ''
while True:
    nome = str(input('Digite o nome do produto: ')).strip()
    preco = float(input('Digite o preço: R$ '))
    if preco > 0:
        menorpreco = preco
        total += preco
        if preco < menorpreco:
            menorpreco = preco
            nomemaisbarato = nome
        if preco > 1000:
            maisdemil += 1
        escolha = str(input('Quer continuar? [S/N]: ')).strip().upper()
        if escolha == 'N':
            break
    else:
        preco = float(input('''Preço inválido, tente novamente:
    Digite o preço: '''))
print('-'*10, 'RESULTADO', '-'*10)
print('O total foi de: R${:.2f}'.format(total))
print(f'{maisdemil} produtos custaram mais de mil reais.')
print('O produto mais barato foi : {} e custou R${:.2f}'.format(nomemaisbarato, menorpreco))
