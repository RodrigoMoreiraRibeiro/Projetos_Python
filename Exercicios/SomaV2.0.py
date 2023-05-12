s = 0
cont = 0
for c in range(1, 500, 2):
    print(c)
    if  c % 3 == 0:
        s =+ c
        cont = cont + 1

print(f'A soma de todos so {cont} valores solicitados é {s}')