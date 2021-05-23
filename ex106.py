# Sistema interativo de ajuda em Python
from time import sleep
print('\033[32:40m-'*20)
print('Sistema de Ajuda')
print('-'*20)
sleep(1)
resp = str(input('Função ou biblioteca: ')).strip().lower()
print('-'*20)
print('ANALISANDO...')
print('-'*20)
sleep(1)
print('\033[32:40m')
help(resp)