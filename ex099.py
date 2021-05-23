# Função que descobre o maior
from time import sleep
def maior(* num):
    cont = maior = 0
    print('Analisando os valores...')
    for valor in num:
        print(f'{valor}', end=' ')
        sleep(0.3)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f'Foram informados {cont} valores.')
    print(f'O maior valor informado foi {maior}')


maior(2,9,4,5,1)