# Jogo da advinhação v1.0

from random import randrange
n = randrange(0, 5)
resp = int(input('Tente advinhar o numero entre 0 a 5: '))
if resp == n:
    print('Você acertou!!')
else:
    print('Sinto muito, você errou.')


