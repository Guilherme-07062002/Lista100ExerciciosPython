# Lista composta e analise de dados
pessoas = list()
dados = list()
resposta = ''
maior = list()
menor = list()
quantpessoas = cont = maiorpeso = menorpeso = 0
while True:
    nome = str(input('Digite o nome: '))
    dados.append(nome)
    peso = int(input('Digite a peso: '))
    dados.append(peso)
    cont += 1
    if cont == 1:
        maiorpeso = peso
        menorpeso = peso
    else:
        if peso > maiorpeso:
            maiorpeso = peso
            maior.append(nome)
        elif peso < menorpeso:
            menorpeso = peso
            menor.append(nome)

    pessoas.append(dados[:])
    quantpessoas += 1
    dados.clear()
    resposta = str(input('Quer continuar?[S/N] ')).strip().upper()
    if resposta == 'N':
        break

print(pessoas)
print(f'{quantpessoas} pessoas foram cadastradas')
print(f'Os maior peso foi de {maiorpeso}Kg, peso de: ',end=' ')
for p in pessoas:
    if p[1] == maiorpeso:
        print(f'[{p[0]}]',end=' ')
print()
print(f'Os menor peso foi de {menorpeso}Kg, peso de : ', end=' ')
for p in pessoas:
    if p[1] == menorpeso:
        print(f'[{p[0]}]', end=' ')
print()
