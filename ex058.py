# Jogo da advinhação 2.0
from random import randint
robo = randint(0, 10)
tentativas = 0
numero = int(input('Tente advinhar o numero que pensei: '))
while numero != robo:
    numero = int(input('\033[31mErrado, tente novamente: '))
    tentativas += 1

if numero == robo:
    print('\033[32mParabéns! Depois de {} tentativas você advinhou que era o numero \033[34m{}\033[m.'.format(tentativas, robo,tentativas))
