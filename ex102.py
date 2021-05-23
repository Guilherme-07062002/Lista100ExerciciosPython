# Função para fatorial
def fatorial(num, show = 0):
    """
    :param num: O número que será calculado.
    :param show: (Opcional) Mostrar ou não mostrar a conta.
    :return: O valor do fatorial de um número n.
    """
    f = 1
    for c in range(num, 0, -1):
        if show == True:
            print('|',c, end=' | ')
        f *= c
    return f
'help(fatorial)'
print('-' * 20)
print(f'Resultado: {fatorial(3,True)}')