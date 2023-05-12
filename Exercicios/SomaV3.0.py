
n = 0
soma = 0
cont = 0
while True:
    n = int(input('Digite um numero: '))
    cont += 1
    soma = soma + n
    if n == 999:
        cont1 = cont - 1
        print(f'Voce digitou {cont1} Números e a soma entre ele foi: {soma - 999}')

        break









