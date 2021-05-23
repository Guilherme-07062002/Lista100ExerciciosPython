# Cadastro de trabalhador em python
from datetime import date
dicionario = {'Nome':'','Ano de nascimento':0,'Carteira de trabalho':''}
dicionario['Nome'] = str(input('Digite o nome: '))
dicionario['Ano de nascimento'] = int(input('Digite ano de nascimento: '))
ctps =  int(input('Digite CTPS: '))
dicionario['Carteira de trabalho'] = ctps
if ctps != 0:
    dicionario['Ano de contratação'] = int(input('Digite o ano de contratação: '))
    dicionario['Salario'] = float(input('Digite o salário: '))
dicionario['Idade'] =  date.today().year - dicionario['Ano de nascimento']
print('-'*10,'DADOS','-'*10)
for k, v in dicionario.items():
    print(f'{k} = {v}')
