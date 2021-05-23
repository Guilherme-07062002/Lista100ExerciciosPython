# Aumentos multiplos

salario = float(input('Informe o salario: '))
dezp = 10/100 * salario
quinzep = 15/100 * salario
if salario > 1.250:
    print('Você terá um aumento de 10% logo o total: R${:.2f}'.format(dezp + salario))
else:
    print('Você terá um aumento de 15% logo o total: R${:.2f}'.format(quinzep))
