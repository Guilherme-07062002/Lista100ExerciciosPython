# Formatando moedas em Python
from ex108 import moeda

p = float(input('Digite o preço: R$'))
print(f'A metade de {moeda.moeda(p)} é: {moeda.moeda(moeda.metade(p))}')
print(f'O dobro de {moeda.moeda(p)} é: {moeda.moeda(moeda.dobro(p))}')
print(f'Aumentando 10%: {moeda.moeda(moeda.aumentar(p,10))}')
print(f'Diminuindo 13%: {moeda.moeda(moeda.diminuir(p,13))}')
print(f'Formatado: {moeda.moeda(p)}')