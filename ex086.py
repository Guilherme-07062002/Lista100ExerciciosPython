# Matriz em python
matriz = [[0,0,0],[0,0,0],[0,0,0]]
for c in range(0,3):
    for l in range(0,3):
        matriz[l][c]= int((input('Digite um numero: ')))
for c in range(0, 3):
    for l in range(0,3):
        print(f'[{matriz[l][c]:^5}]',end=' ')
    print()