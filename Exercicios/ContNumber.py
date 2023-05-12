'''n1 = int(input('Digite um numero: '))
n2 = int(input('Digite um numero: '))
n3 = int(input('Digite um numero: '))
n4 = int(input('Digite um numero: '))'''
print('='*50)
num =  (int(input('Digite um número: ')),
        int(input('Digite um número: ')),
        int(input('Digite um número: ')),
        int(input('Digite um número: ')))
print(f'Voce digitou {num}')

print('='*50)
print(f'Apareceu o número 9 {num.count(9)} vezes')
print('='*50)

if num == 3:
    print(f'O primeiro número 3 foi digitado na {num.index(3) + 1}º posição')
else:
    print('O valor 3 não foi digitado')

print('='*50)

for n in num:
    if n % 2 == 0:
        print(n, end=' ')

'''if num[0] % 2 == 0:
    print(num[0], end=' -> ')
if num[1] % 2 == 0:
    print(num[1], end=' -> ')
if num[2] % 2 == 0:
    print(num[2], end=' -> ')
if num[3] % 2 == 0:
    print(num[3], end=' -> ')'''

print('Foram os números pares digitados ')