lista = []
maior = cont = posmenor = posmaior = 0
for c in range(0, 5):
    lista.append(int(input('Digite um número: ')))
    cont += 1
    if cont == 1:
        menor = maior = lista[c]
    else:
        if lista[c] < menor:
            menor = lista[c]
        elif lista[c] > maior:
            maior = lista[c]
print(lista)
print(f'O maior numero é {maior} na posições: ',end=' ')
for i, v in enumerate(lista):
    if lista[i] == maior:
        print(f'{i}...', end=' ')
print(f'\nO menor numero é {menor} na posições: ', end=' ')
for i, v in enumerate(lista):
    if lista[i] == menor:
        print(f'{i}...',end=' ')