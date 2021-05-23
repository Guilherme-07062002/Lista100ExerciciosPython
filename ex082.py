lista = []
par = []
impar = []
resposta = 'S'
num = 0
while resposta == "S":
    num = int(input('Digite um número: '))
    lista.append(num)
    if num % 2 == 0:
        par.append(num)
    elif num % 2 == 1:
        impar.append(num)
    resposta = str(input('Quer continuar?[S/N] ')).strip().upper()
print(f'A lista de todos os numeros digitados: {lista}')
print(f'A lista de pares: {par}')
print(f'A lista de impares: {impar}')