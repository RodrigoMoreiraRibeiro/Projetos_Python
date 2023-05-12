import math
kg = float(input('Digite seu Peso: '))
alt = float(input('Digite sua altura em cm: '))
m = alt / 100

imc = kg / m**2


if imc < 18.5:
    print(f'Seu imc é {imc:.2f}')
    print('Abaixo do Peso!!!')
elif imc >= 18.5 and imc < 25:
    print(f'Seu imc é {imc:.2f}')
    print('Peso ideal!!!')
elif imc >= 25 and imc < 30:
    print(f'Seu imc é {imc:.2f}')
    print('Você está sobrepeso')
elif imc >= 30 and imc < 40:
    print(f'Seu imc é {imc:.2f}')
    print('Você está em Obesidade!!!')
elif imc > 40:
    print(f'Seu imc é {imc:.2f}')
    print('Obesidade Mórbbida!!!')
