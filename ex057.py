# Validação de dados
sexo = 'M'
while sexo == 'M' or sexo == 'F' and sexo != 'F' or sexo != 'M':
    if sexo != 'M' and sexo != 'F':
        sexo = str(input('Resposta inválida, tente novamente: ')).strip().upper()
    else:
        sexo = str(input('Insira o sexo [M,F]: ')).strip().upper()
