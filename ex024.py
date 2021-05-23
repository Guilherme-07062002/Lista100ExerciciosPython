# Verificando as primeiras letras de um texto
cidade = str(input('Digite o nome de uma cidade: ')).strip()
print('True = Começa com Santo\nFalse = Não começa')

cidade = cidade.upper()
div = cidade.split()
print('SANTO' in div[0])
