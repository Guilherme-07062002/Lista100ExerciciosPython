# Mais sobre matriz em pyhon
matriz = [[0,0,0],[0,0,0],[0,0,0]]
soma = somapar = maior =  0
for c in range(0, 3):
    for l in range(0, 3):
        matriz[c][l] = int(input(f'Digite um número para a posição [{c},{l}]: '))
for c in range(0, 3):
    for l in range(0,3):
        print(f'[{matriz[c][l]:^5}]',end=' ')
        soma += matriz[c][l]
        if matriz[c][l] % 2 == 0:
            somapar += matriz[c][l]
        if matriz[l] == 2:
            maior = matriz[c][l]
        elif matriz[c][l] > maior:
            maior = matriz[c][l]
    print(f' = {soma}',end=' ')
    soma = 0
    print()
print(f'A soma dos pares é: {somapar} ')
print(f'O maior numero da segunda linha é: {maior}')