# Detector de palindromo
frase = str(input('Digite uma frase para saber se ela é um palindromo: ')).strip()
cont = frase.count(' ')
n = 0
if cont > 0:
    frase = frase.split()
    frase = ','.join(frase)

pal = frase[::-1]
if pal.upper() == frase.upper():
    print('\033[34m{}\033[m de trás pra frente é \033[34m{}\033[m\nLogo, é um palidromo.'.format(frase.upper().replace(',', ' '), pal.upper().replace(',', ' ')))
else:
    print('\033[34m{}\033[m de trás pra frente é \033[34m{}\033[m \nLogo, \033[31mNÃO\033[m é um palindromo.'.format(frase.upper().replace(',', ' '), pal.upper().replace(',' , ' ')))




