# Analisador de Textos:
nome = str(input('Digite seu nome completo: ')).strip()
print('Em maiusculo: {} '.format(nome.upper()))
print('Em minusculo: {} '.format(nome.lower()))

div = nome.split()
print('O nome tem {} letras'.format(len(nome) - nome.count(' ')))
print('O seu primeiro nome é {} e tem {} letras'.format(div[0], len(div[0])))
