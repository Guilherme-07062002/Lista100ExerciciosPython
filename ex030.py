# Par ou impar
from colorama import Fore, Style

n = int(input(Fore.BLUE +'Digite um numero: '))
if n % 2 == 0:
    print(Fore.WHITE + 'O numero {} é'.format(n) + Fore.GREEN + ' PAR')
else:
    print(Fore.WHITE + 'O numero {} é'.format(n) + Fore.RED + ' IMPAR')
