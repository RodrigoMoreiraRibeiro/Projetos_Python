cont = 0
soma = 0
while True:
    n = int(input('Digite um número: (999 Para parar) '))
    if n == 999:
        break
    soma += n
    cont += 1
print(f'Foram digitos {cont} números e a soma foi de {soma}')
