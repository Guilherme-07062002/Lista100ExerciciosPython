# PEDRA PAPEL TESOURA
from random import choice

escolha = int(input('O que você escolhe?\n'
                    '0 = pedra\n'
                    '1 = papel\n'
                    '2 = tesoura\n'
                    'Digite aqui: '))
opcoes = 'Pedra Papel Tesoura'
opcoes = opcoes.split()
lista = [0, 1, 2]
robo = choice(lista)
if robo == escolha:
    print('O robô colocou {} e você colocou {}\nEMPATE'.format(opcoes[robo], opcoes[escolha]))
elif robo == 1 and escolha == 0:
    print('O robô colocou {} e você colocou {}\nDERROTA'.format(opcoes[robo], opcoes[escolha]))
elif robo == 0 and escolha == 1:
    print('O robô colocou {} e você colocou {}\nVITORIA'.format(opcoes[robo], opcoes[escolha]))
elif robo == 2 and escolha == 0:
    print('O robô colocou {} e você colocou {}\nVITORIA'.format(opcoes[robo], opcoes[escolha]))
elif robo == 0 and escolha == 2:
    print('O robô colocou {} e você colocou {}\nDERROTA'.format(opcoes[robo], opcoes[escolha]))
elif robo == 2 and escolha == 1:
    print('O robô colocou {} e você colocou {}\nDERROTA'.format(opcoes[robo], opcoes[escolha]))
elif robo == 1 and escolha == 2:
    print('O robô colocou {} e você colocou {}\nVITORIA'.format(opcoes[robo], opcoes[escolha]))
else:
    print('Escolha inválida.')
