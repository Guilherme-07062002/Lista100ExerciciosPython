# Calculando desconto
p = float(input('Digite o preço do produto R$'))
desc = (5 / 100) * p
r = p - desc
print('Preço com 5% de desconto: R${:.2f}'.format(r))
