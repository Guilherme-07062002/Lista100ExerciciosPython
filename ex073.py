# Tuplas com time de Futebol
lista = ('Flamengo','Internacional','Atletico-MG','São Paulo'
         ,'Fluminense','Gremio','Palmeiras','Santos','Athletico-PR'
         ,'Bragantino','Ceará SC','Corinthias','Atletico-GO'
         ,'Bahia','Sport Recife','Fortaleza','Vasco da Gama'
         ,'Goiás', 'Coritiba', 'Botafogo')
print('----Os cinco primeiros colocados----')
print(lista[0:5])
print('-----Os ultimos quatro----')
print(lista[-4:])
print('----Em ordem alfabética----')
print(sorted(lista))
cont = 0
for c in range(len(lista)):
    if lista[cont] == 'Palmeiras':
        print(f'O Palmeiras está na {cont + 1}° posição.')
    cont += 1