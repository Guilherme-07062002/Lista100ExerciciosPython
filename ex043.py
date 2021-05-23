# Indice de massa corporal
peso = float(input('Insira seu peso (kg): '))
altura = float(input('Insira a altura (m): '))
imc = peso / (altura ** 2)
if imc < 18.5:
    print('\033[34mAbaixo do peso.')
elif imc >= 18.5 and imc < 25:
    print('\033[34mPeso ideal.')
elif imc >= 25 and imc < 30:
    print('\033[34mSobrepeso.')
elif imc >= 30 and imc < 40:
    print('\033[34mObesidade.')
elif imc >= 40:
    print('\033[34mObesidade mórbida.')