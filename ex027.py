# Primeiro e ultimo nome de uma pessoa
nome = str(input('Digite seu nome completo: ')).strip()
div = nome.split()
print('primeiro = {} '.format(div[0]))
print('ultimo = {} '.format(div[len(div) - 1]))
