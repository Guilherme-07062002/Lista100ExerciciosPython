# Catetos e hipotenusa
from math import sqrt, floor

catad = float(input('Digite o valor do cateto adjascente: '))
catop = float(input('Digite o valor do cateto oposto'))
hipoten = (catop ** 2) + (catad ** 2)
res = sqrt(hipoten)
print('O valor do comprimento da hipotenusa é: {:.2f}'.format(res))
