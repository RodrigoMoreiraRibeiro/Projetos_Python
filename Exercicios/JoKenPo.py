from random import randint
from time import sleep

lista = ('Pedra', 'Papel', 'Tesoura')

maquina = randint(0, 2)

print('[0] Pedra')
print('[1] Papel')
print('[2] Tesoura')

p1 = int(input('Escoolha uma opção: '))

print('JO\n')
sleep(1)
print('KEN\n')
sleep(1)
print('PO\n')

print(f'A maquina escolheu {lista[maquina]}')
print(f'o player escolheu {lista[p1]}')

if maquina == 0:
    if p1 == 0:
        print('Empate!!!')
    elif p1 == 1:
        print('Player Ganhou!!!')
    elif p1 == 2:
        print('Player perdeu')
    else:
        print('Operação inválida')

elif maquina == 1:
    if p1 == 0:
        print('Player Perdeu!!!')
    elif p1 == 1:
        print('Empate!!!')
    elif p1 == 2:
        print('Player Ganhou!!!')
    else:
        print('Operação inválida')

elif maquina == 2:
    if p1 == 0:
        print('Plaer Ganhou!!!')
    elif p1 == 1:
        print('Player Perdeu!!!')
    elif p1 == 2:
        print('Empate!!!')
    else:
        print('Operação inválida')

else:
    print("Operação inválida")







