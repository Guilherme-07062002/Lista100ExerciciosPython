# Gerenciador de pagamentos
preco = float(input('Digite o preço do produto: R$'))
cond = int(input('Selecione a condição de pagamento:'
                 '\n1 = À vista dinheiro/cheque;'
                 '\n2 = À vista no cartão;'
                 '\n3 = Em até 2x no cartão;'
                 '\n4 = 3x ou mais no cartão;'
                 '\nDigite aqui: '))
if cond == 1:
    print('O valor de R${:.2f} terá 10% de desconto ficando: {}R${:.2f}{}'.format(preco, '\033[34m', preco - preco * (10/100),'\033[34m'))
elif cond == 2:
    print('O valor de R${:.2f} terá 5% de desconto ficando: {}R${:.2f}{}'.format(preco, '\033[34m',preco - preco * (5 /100), '\033[m'))
elif cond == 3:
    print('O valor será o preço normal de: {}R${:.2f}{}'.format('\033[34m', preco, '\033[m'))
elif cond == 4:
    print('O valor de R${:.2f} terá um juros de 20%, ficando: {}R${:.2f}{}'.format(preco,'\033[34m', preco + preco * (20/100),'\033[m'))
