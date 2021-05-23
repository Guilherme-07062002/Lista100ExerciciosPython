# Classificar atletas
from datetime import date

ano = int(input('Insira o ano de nascimento para saber a categoria: '))
dif = date.today().year - ano
if 0 < dif <= 9:
    print('O atleta tem {} anos\nMIRIM'.format(dif))
elif 10 <= dif <= 14:
    print('O atleta tem {} anos\nINFANTIL'.format(dif))
elif 15 <= dif <= 19:
    print('O atleta tem {} anos\nJUNIOR'.format(dif))
elif dif == 20:
    print('O atleta tem {} anos\nSENIOR'.format(dif))
elif dif > 20:
    print('O atleta tem {} anos\nMASTER'.format(dif))
