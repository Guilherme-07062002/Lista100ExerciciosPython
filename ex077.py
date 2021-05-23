# Contando vogais em tupla
palavras= ('aprender','programar','linguagem','python'
         ,'curso','gratis','estudar','praticar',
         'trabalhar','mercado','programador','futuro')
vogais = ('a','e','i','o','u')
for p in palavras:
    print(f'\nNa palavra {p.upper()} temos ',end=' ')
    for letra in p:
        if letra.lower() in'aeiou':
            print(letra, end=' ')