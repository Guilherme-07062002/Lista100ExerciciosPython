# Funções para votação
from datetime import date
def voto(ano):

    res = date.today().year - ano
    if res >= 18 and res < 60:
        return f'Com {res} anos: Voto Obrigatorio'
    if res >= 16 and res < 18 or res >= 60:
        return f'Com {res} anos:Voto opcional'
    if res < 16:
        return f'Com {res} anos :Ainda não vota'


ano = int(input('Digite o seu ano de nascimento: '))
print(voto(ano))

'''    print('Voto negado.')
if voto(ano) == 1:
    print('Voto obrigatorio')
if voto(ano) == 2:
    print('Voto opcional')
'''