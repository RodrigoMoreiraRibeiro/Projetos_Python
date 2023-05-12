for c in range(10):
    n = int(input('Digite um numero: '))
    n1 = n % 2

    if n1 == 1:
        print(f'O número {n} é um número Primo!')
    else:
        print('Não é um número primo')

# Solução do CursoEmVideo

'''num = int(input('Digite um número: '))
tot = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[33m', end='')
        tot += 1
    else:
        print('\033[31m', end='')
    print('{} '.format(c), end='')
print(f'\n\033[mO numero {num} foi divisivel tantas {tot} vezes')
if tot == 2:
    print('E por isso ele é PRIMO!')
else:
    print('E por isso ele NÃO É PRIMO')'''
