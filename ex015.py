# Aluguel de carros
km = float(input('Quantos km percorridos?'))
dias = int(input('Quantos dias ele foi alugado?'))
rd = 60 * dias
rkm = 0.15 * km
r = rd + rkm
print('O total a pagar é de : R${:.2f}'.format(r))
