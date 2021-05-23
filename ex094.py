# Unindo dicionarios e listas
pessoas = list()
mulheres = list()
idadeacimamedia = list()
dados = dict()
quant = somaidade = idade =  0
while True:
    nome = str(input('Digite o nome:'))
    dados['Nome'] = nome
    sexo = str(input('Digite o sexo [M/F]: ')).upper()
    dados['Sexo'] = sexo
    if sexo in 'Ff':
        mulheres.append(nome)
    idade = int(input('Digite a idade: '))
    dados['Idade'] = idade
    somaidade += idade
    pessoas.append(dados.copy())
    quant += 1
    resposta = str(input('Quer continuar? '))
    if resposta in 'Nn':
        break
mediaidade = somaidade/ quant
for p in pessoas:
    print(p)

for c in dados.values():
    if dados['Idade'] > mediaidade:
        if dados['Nome'] not in idadeacimamedia:
            idadeacimamedia.append(dados['Nome'])
print(f'{quant} pessoas foram cadastradas.')
print(f'A média entre as idades é {mediaidade:.2f}')
print(f'Lista de mulheres cadastradas: {mulheres}')
print(f'Lista de pessoas com idade acima da média: {idadeacimamedia}')


