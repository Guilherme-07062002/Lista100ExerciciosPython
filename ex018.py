# Seno, cosseno e tangente
from math import sin, cos, tan, radians

grau = float(input('Digite o valor do grau para saber o seu sen, cos e tg: '))
s = sin(radians(grau))
c = cos(radians(grau))
t = tan(radians(grau))

print('O valor de {}° em:\n seno: {:.2f}\n cosseno: {:.2f}\n tangente: {:.2f}'.format(grau, s, c, t))




