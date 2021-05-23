# Jogo de dados em Python
from random import randint
from time import sleep
from operator import itemgetter
jogo = {'Jogador 1': randint(1, 6),
        'Jogador 2': randint(1, 6),
        'Jogador 3': randint(1, 6),
        'Jogador 4': randint(1, 6)}
ranking = dict()
for j, v in jogo.items():
    print(f'{j} = {v}')
    sleep(1)
ranking = sorted(jogo.items(), key= itemgetter(1), reverse= True)
cont = 1
for j, v in ranking:
    print(f'{cont}° Lugar: {j} que tirou = {v}')
    cont += 1