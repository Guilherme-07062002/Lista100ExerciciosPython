lista = []
resposta = 'S'
quant = cinco = 0
while resposta == 'S':
    num = int(input('Digite um número: '))
    lista.append(num)
    quant += 1
    if num == 5:
        cinco = 1
    resposta = str(input('Quer continuar?[S/N] ')).strip().upper()
print(lista)
print(f'Você digitou {quant} números')
lista.sort(reverse= True)
print(f'Ao contrário eles ficam {lista}')
if cinco == 1:
    print('O numero 5 foi digitado e está na lista.')
else:
    print('O número 5 não foi digitado e não está na lista.')