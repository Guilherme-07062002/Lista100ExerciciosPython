# Sorteando uma ordem na lista
from random import shuffle

n1 =input('Insira um nome: ')
n2 =input('Insira um nome: ')
n3 =input('Insira um nome: ')
n4 =input('Insira um nome: ')

lista = [n1, n2, n3, n4]
shuffle(lista)

print('Os aluno em ordem: {}'.format(lista))
