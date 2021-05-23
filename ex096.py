# Função que calcula area
def area(larg, comp):
    area = larg * comp
    print(f'Um terreno de dimensões {larg}x{comp} tem {area}m² de area.')


larg = float(input('Digite a largura: '))
comp = float(input('Digite o comprimento: '))
area(larg, comp)