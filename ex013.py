# Reajuste salarial
n = float(input('Digite seu salário R$'))
aum = (15/100) * n
r = aum + n
#:.2f Limita o numero depois da virgula a duas casas decimais
print('Seu novo salário com aumento é: R${:.2f}'.format(r))
