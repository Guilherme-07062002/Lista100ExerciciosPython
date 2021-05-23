# Aprovando emprestimo
valor = float(input('Insira o valor da casa: '))
salario = float(input('Digite o salário do comprador: '))
ano = int(input('Em quantos anos o pagamento será feito? '))

prestacao = valor / ano

if prestacao > salario * (30/100):
    print('\033[31mEmpréstimo negado')
else:
    print('\033[32mEmprestimo aceito')