'''cont = 0
tab = 0
while True:
    n = int(input('Digite o número que deseja da Tabuada: '))
    if n > 0:
        while tab < 10:
            tab += 1
            mult = n * tab
            cont += 1
            print(f'{n} x {tab} = {mult}')

            continue
        tab -= 10

    if n < 0:
        break
print('Programa Tabuada ENCERRADO!!!')'''

# solução Curso em Video
while True:
    n = int(input('Digite o número que deseja da Tabuada: '))
    if n < 0:
        break
    for c in range(1, 11):
        print(f'{n} x {c} = {n*c}')

print('Programa TABUADA ENCERRADO!!!')