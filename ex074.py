# Maior e menor valores em tupla
from random import randint
tupla = (0,0,0,0,0)
menor = maior = 0
for c in range(0, 5):
    aleatorio = randint(1, 10)
    tupla = aleatorio
    menor = tupla
    print(tupla, end=' ')
    if tupla > menor:
        menor = tupla
    elif tupla > maior:
        maior = tupla
print(f'\nO menor valor é: {menor}')
print(f'O maior valor é: {maior}')