# Analise de dados em uma tupla
n1 = int(input('Digite o 1° numero: '))
n2 = int(input('Digite o 2° numero: '))
n3 = int(input('Digite o 3° numero: '))
n4 = int(input('Digite o 4° numero: '))
tupla = (n1, n2, n3, n4)
cont = pares = 0
for c in range(len(tupla)):
    if cont <=4:
        if tupla[c] % 2 == 0:
            pares +=1
    cont +=1
print('Você digitou: ',tupla)
print('O numero 9 apareceu  {} vezes'.format(tupla.count(9)))
print('O numero 3 aparece primeiro no indice {}'.format(tupla.index(3)))
print(f'A quantidade de numeros pares é: {pares}')