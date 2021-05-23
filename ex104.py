# Validando entrada de dados
def leiaint(msg):
    ok = False
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print(f'\033[31mERRO, DIGITE UM NÚMERO INTEIRO VALIDO\033[m')
        if ok:
            break
    return valor


n = leiaint('Digite um número: ')
print(f'Você digitou o numero {n}')
