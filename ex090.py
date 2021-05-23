# Dicionario em python
lista = list()
dados = {'Nome':'','Média': 0,'Situação':''}

dados['Nome'] = str(input('Digite o nome do aluno: ')).strip()
dados['Média'] = float(input('Digite a média do aluno. '))
if dados['Média'] >= 7:
    dados['Situação'] ='Aprovado'
    lista.append(dados.copy())
if dados['Média'] < 7:
    dados['Situação'] = 'Reprovado'
    lista.append(dados.copy())
print('-'*30)
for a,n in dados.items():
    print(f'{a} == {n}')
