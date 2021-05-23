# Formatando moedas em python
from ex109 import moeda

p = float(input('Digite o preço: R$'))
print(f'A metade de {moeda.moeda(p)} é: {moeda.metade(p,True)}')
print(f'O dobro de {moeda.moeda(p)} é: {moeda.dobro(p,True)}')
print(f'Aumentando 10%: {moeda.aumentar(p,10,True)}')
print(f'Diminuindo 13%: {moeda.diminuir(p,13,True)}')
print(f'Formatado: {moeda.moeda(p)}')