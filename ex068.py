# Jogo do par ou impar
from random import randint
soma = vitorias = 0
opcao = ['PAR', 'IMPAR']
robo = randint(1, 10)
while True:
   escolha = str(input('Escolha par ou impar: ')).strip().upper()
   num = int(input('Digite um número: '))
   print('-' * 20)
   soma = num + robo
   if soma % 2 == 0 and escolha == 'PAR':
       print(f'''O robô jogou {robo} e você {num}
{soma} é PAR
VITORIA
{'-' * 20}''')
       vitorias += 1
   elif soma % 2 == 1 and escolha == 'IMPAR':
       print(f'''O rôbô jogou {robo} e você {num}
{soma} é IMPAR
VITORIA
{'-' * 20}''')
       vitorias += 1
   else:
       break
if soma % 2 == 0 and escolha == 'IMPAR':
       print(f'''O robô jogou {robo} e você {num}
{soma} é PAR
DERROTA
Você venceu {vitorias} vezes consecutivas.
{'-' * 20}''')
elif soma % 2 == 1 and escolha == 'PAR':
       print(f'''O rôbô jogou {robo} e você {num}
{soma} é IMPAR
DERROTA
Você venceu {vitorias} vezes consecutivas
{'-' * 20}''')
