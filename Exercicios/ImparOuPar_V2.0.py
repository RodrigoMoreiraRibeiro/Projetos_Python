from random import randint
v = 0
while True:
    maq = randint(0, 10)
    esc = int(input('''
    [1] IMPAR
    [2] PAR
    Escolha IMPAR ou PAR >>> '''))

    if esc != 1 and esc != 2:
        print('Opção inválida, Tente novamente!')
        continue

    p1 = int(input('Agora escolha um número: '))
    soma = maq + p1

    if esc == 1:
        div = soma % 2
        if div == 1:
            print('Voce ganhou, Vá denovo!!')
            print(f'{p1} + {maq} = {soma}')
            v += 1
            continue
        else:
            print('Voce Perdeu!, Acabou sua chance!')
            print(f'{p1} + {maq} = {soma}')
            break

    if esc == 2:
        div = soma % 2
        if div == 0:
            print('Voce ganhou, Vá denovo!!')
            print(f'{p1} + {maq} = {soma}')
            v += 1
            continue
        else:
            print('Voce Perdeu!, Acabou sua chance!')
            print(f'{p1} + {maq} = {soma}')
        break

print(f'Voce venceu a maquina {v} vezes')
