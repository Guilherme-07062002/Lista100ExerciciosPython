def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError,  TypeError):
            print(f'Erro, tente novamente.')
            continue
        else:
            return n


def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print(f'ERRO, tente novamente.')
            continue
        else:
            return n


#num = leiaInt('Digite um valor: ')
#print(f'O valor digitado foi {num}')
num = leiaFloat('Digite um valor: ')
print(f'O valor digitado foi {num}')