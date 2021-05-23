# Pintando parede
alt = float(input('Digite a altura:'))
larg = float(input('Digite a largura:'))
area = alt * larg
total = area / 2
print('Sua parede tem a dimensão de {}x{} e uma area de {}m²\n'
      'Serão necessários {} litros de tinta'
      .format(alt, larg, area, total))
