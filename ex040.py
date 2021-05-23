# Média
n1 = float(input('Insira a primeira nota: '))
n2 = float(input('Insira a segunda nota: '))
media = (n1 + n2)/2
if media < 5:
    print('\033[31mSinto muito, Você foi reprovado!')
elif 5 < media < 6.9:
    print('\033[34mVocê está de recuperação.')
elif media >= 7:
    print('\033[32mParabéns!! Você foi aprovado.')