# Contagem Regressiva
from time import sleep

n = 11
for c in range(n, 1, -1):
    n -= 1
    print(n)
    sleep(1)
print('\033[032mFELIZ ANO NOVO!!')
