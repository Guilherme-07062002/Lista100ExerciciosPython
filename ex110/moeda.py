def aumentar(n = 0,p = 0, formato = False):
    porc = n * (p/100)
    res = n + porc
    return res if formato is False else moeda(res)

def diminuir(n = 0,p = 0, formato = False):
    porc = n * (p/100)
    res = n - porc
    return res if formato is False else moeda(res)


def dobro(n = 0, formato = False):
    n *= 2
    return n if not formato else moeda(n)


def metade(n = 0, formato = False):
    n /= 2
    return n if not formato else moeda(n)


def moeda(preco = 0,moeda = 'R$'):
    return f'{moeda}{preco:>8.2f}'.replace('.', ',')

def resumo(p = 0, taxaa = 10, taxar = 5):
    print('-'*30)
    print('RESUMO DO VALOR'.center(30))
    print('-'*30)
    print(f'Preço analisado: \t{moeda(p)}')
    print(f'Dobro do preço: \t{dobro(p,True)}')
    print(f'Metade do preço: \t{metade(p,True)}')
    print(f'{taxaa}% de aumento : \t{aumentar(p,taxaa,True)}')
    print(f'{taxar}% de aumento : \t{diminuir(p,taxar, True)}')
    print('-'*30)
