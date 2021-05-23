# Alistamento militar:
from datetime import date

ano = int(input('Digite o ano de seu nascimento: '))
dif = date.today().year - ano
if dif == 18:
    print('\033[32mEstá no ano de você se alistar.')
elif dif > 18:
    print('\033[31mJá passaram: {} ano(s) do ano de seu alistamento.'.format(dif - 18))
else:
    print('\033[34mAinda não é o ano do seu alistamento\nFaltam {} ano(s) para seu alistamento ({})'.format(18 - dif, date.today().year + (18 - dif)))

