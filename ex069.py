# Analise de dados do grupo
idade = maior = homens = mulheres = 0
sexo = ''
escolha = ''
while True:
    print('-' * 10, 'CADASTRO', '-' * 10)
    idade = int(input('Digite a idade: '))
    sexo = str(input('Digite o sexo[M/F]: ')).upper().strip()
    if idade > 18:
        maior += 1
    if sexo != 'M' and sexo != 'F':
        sexo = str(input('''Sexo inválido, tente novamente.
Digite o sexo[M/F]: ''')).strip().upper()
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        mulheres += 1
    escolha = str(input('Quer continuar?[S/N] ')).strip().upper()
    if escolha == 'N':
        print('-' * 10 , 'FIM', '-' * 10)
        break
print(f'{maior} pessoas tem mais de 18 anos.')
print(f'{homens} homens foram cadastrados.')
print(f'{mulheres} mulheres tem menos de 20 anos.')