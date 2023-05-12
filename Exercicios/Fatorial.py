'''n = int(input('Digite um valor:'))
fat = 1
i = 1

while i <= n:
    fat = fat * i
    i = i + 1

print(f'O fatorial de {n} é = {fat} ')'''

# Solução Curso em video

'''from math import factorial
n = int(input('Digite um número para calcular seu Fatorial: '))
f = factorial(n)
print(f'O fatorial de {n} é {f}')'''

from time import sleep
n = int(input('Digite um número para calcular seu Fatorial: '))
c = n
f = 1
print(f'Calculando {c}! = ', end='')

sleep(2)

while c > 0:

    print(f'{c} ', end='')
    print('x ' if c > 1 else ' = ', end= '')
    f *= c
    c -= 1

print(f'{f}')



