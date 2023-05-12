s = 0
cont = 0
for c in range(1, 7):
    num = int(input(f'Digite o {c} valor: '))
    if num % 2 == 0:
        s += num
        cont += 1
print(f'Voce informou {cont} Pares números e a soma foi {s}')
