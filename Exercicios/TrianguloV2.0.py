r1 = float(input('Digite um lado: '))
r2 = float(input('Digite outro lado: '))
r3 = float(input('Digite outro lado: '))


if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Podem formar um triangulo: ')
    if r1 == r2 == r3:
        print('É um triangulo Equilátero')
    elif r1 == r2 or r1 == r3 or r2 == r3:
        print('É um triangulo isósceles')
    else:
        print('É um triangulo Escaleno')
else:
    print('Não podem formar um trinagulo')
