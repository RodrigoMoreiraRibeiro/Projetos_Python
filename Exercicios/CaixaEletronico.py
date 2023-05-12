'''while True:
    n = int(input('Qual valor deseja Sacar? R$ '))

    fifty = int(n / 50)
    n -= (fifty * 50)

    vinte = int(n / 20)
    n -= (vinte * 20)

    ten = int(n / 10)
    n -= (ten * 10)

    um = n

    print(f'\nSerá necessario {fifty} cédulas de R$50.00')
    print(f'Será necessario {vinte} cédulas de R$20.00')
    print(f'Será necessario {ten} cédulas de R$10.00')
    print(f'Será necessario {um} moedas de R$1.00')

    rsp = str(input('\nDeseja Sacar mais? [S/N]  ')).strip().upper()[0]

    if rsp == 'S':
        continue
    if rsp == 'N':
        break
    else:
        print('Opção inválida, Tente novamente!')
print('Programa Encerrado!')'''

# Solução Curso em Video
val = int(input('Qual valor deseja Sacar? R$ '))
tot = val
ced = 50
totced = 0

while True:
    if tot >= ced:
        tot -= ced
        totced += 1
    else:
        if totced > 0:
            print(f'Total de {totced} cedulas de R${ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0
        if tot == 0:
            break

