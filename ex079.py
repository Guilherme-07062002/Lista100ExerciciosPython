resposta = 'S'
lista = []
while resposta == 'S':
   num = int(input('Digite um número: '))
   if num in lista:
       print('Numero repetido, não será adicionado.')
   else:
       lista.append(num)
       resposta = str(input('Quer continuar?[S/N] ')).strip().upper()

print('Fim da operação')
lista.sort()
print(f'Valores digitados: {lista}')