# Primeira e ultima ocorrencia de uma string
frase = str(input('Digite um frase: ')).strip()
frase = frase.upper()
print('A letra "A" aparece {} vezes '.format(frase.count('A')))
print('Ela aparece pela primeira vez na posição: {} '.format(frase.find('A')+1))
print('A ultima letra A apareceu na posição : {}'.format(frase.rfind('A')+1))
