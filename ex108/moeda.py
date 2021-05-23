def aumentar(n = 0,p = 0):
    porc = n * (p/100)
    res = n + porc
    return res

def diminuir(n = 0,p = 0):
    porc = n * (p/100)
    res = n - porc
    return res

def dobro(n = 0):
    n *= 2
    return n

def metade(n = 0):
    n /= 2
    return n


def moeda(preco = 0,moeda = 'R$'):
    return f'{moeda}{preco:>8.2f}'.replace('.', ',')