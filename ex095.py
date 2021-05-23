# Aprimorando os dicionarios
dados = dict()
jogadores = list()
quant = 0
cont = 1
while True:
    dados['Nome'] = str(input('Digite o nome do jogador: '))
    numeroPartidas =  int(input('Digite o número de partidas: '))
    dados['Numero de partidas'] = numeroPartidas
    for c in range(0 , numeroPartidas):
            quant = int(input(f'Digite a quantidade de gols na partida {cont}: '))
            dados[f'Gols na partida {cont}'] = quant
            cont += 1
    dados['Total de gols'] = quant * numeroPartidas
    jogadores.append(dados.copy())
    cont = 1
    escolha = str(input('Quer continuar?[S/N]: '))
    if escolha in 'Nn':
        break
print('-' *20,'DADOS','-' * 20)
for j in jogadores:
    for k,v in dados.items():
        print(f'{k} = {v}')
    print('-' * 20)