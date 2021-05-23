# Ficha do jogador
def ficha(nome = '',gols = 0):
    """
    :param nome: Recebe o nome do jogador.
    :param gols: Recebe o número de gols marcados pelo jogador no campeonato
    Criado por Guilherme Gomes
    """
    if nome == '':
        nome = 'Desconhecido'
    print('-'* 5 , 'DADOS JOGADOR','-'* 5)
    print(f'Nome: {nome}')
    print(f'Número de gol(s): {gols}')
    print('-'*25 )

ficha('Guilherme',15)