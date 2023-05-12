n1 = int(input('Digite o valor 1: '))
n2 = int(input('Digite o valor 2: '))

if n1 > n2:
    print(f'O primeiro valor é o maior!!! {n1}')
elif n2 > n1:
    print(f'O segundo valor é o maior !!! {n2}')
elif n1 == n2 and n2 == n1:
    print(f'Não existe valor maior, {n1} e {n2} são iguais')


