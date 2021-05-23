# Radar eletronico

from colorama import Fore
from colorama import Style

vel = float(input('Insira a velocidade do carro: '))
n = vel - 80
if n > 0:
    print(Fore.RED + Style.BRIGHT + 'Multado por excesso de velocidade.')
    print(Fore.RED + Style.BRIGHT + 'A multa equivale a: R${:.2f}'.format(n * 7.0))
else:
    print(Fore.GREEN + Style.BRIGHT + 'Sem problemas')