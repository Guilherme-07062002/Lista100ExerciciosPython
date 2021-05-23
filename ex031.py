# Custo da viagem

dist = float(input('Insira a distancia da viagem em Km: '))
if dist <= 200:
    print('O preço da viagem será: R${:.2f}'.format(dist * 0.50))
else:
    print('O preço da viagem será: R${:.2f}'.format(dist * 0.45))
