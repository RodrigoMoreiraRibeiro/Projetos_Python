n1 = int(input('Digite um numero: '))
n2 = int(input('Digite outro numero: '))
n3 = int(input('Digite outro numero: '))
# Maior
if n1 > n2 and n1 > n3:
    print('O maior número é {}'.format(n1))
elif n2 > n1 and n2 > n3:
    print('O maior número é {}'.format(n2))
else:
    print('O maior número é {}'.format(n3))
# Menor
if n1 < n2 and n1 < n3:
    print('O menor número é {}'.format(n1))
elif n2 < n1 and n2 < n3:
    print('O menor número é {}'.format(n2))
else:
    print('O menor número é {}'.format(n3))



