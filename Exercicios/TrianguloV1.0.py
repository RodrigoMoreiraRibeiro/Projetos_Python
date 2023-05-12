r1 = float(input('Digite um lado: '))
r2 = float(input('Digite outro lado: '))
r3 = float(input('Digite outro lado: '))


if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('É um triangulo')
else:
    print('Não é um triangulo')
