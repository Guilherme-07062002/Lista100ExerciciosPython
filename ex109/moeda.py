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