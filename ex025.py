# Procurando uma string dentro de outra string
nome = str(input('Digite um nome: ')).strip()
nome = nome.upper()
print('Seu nome tem Silva?: {} '.format('SILVA' in nome.split()))