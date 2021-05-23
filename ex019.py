# Sorteando um item na lista
from random import choice

n1 = input('Digite primeiro nome')
n2 = input('Digite segundo nome')
n3 = input('Digite terceiro nome')
n4 = input('Digite quarto nome')

lista = [n1, n2, n3, n4]
resultado = choice(lista)
print('O aluno sorteado é:{} '.format(resultado))

