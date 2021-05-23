# Pogressão aritmetica v.3.0
num = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))
c = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while c <= total:
        print('{} -'.format(num), end=' ')
        num += razao
        c += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print('Progressão finalizada com {} termos mostrados.'.format(total))