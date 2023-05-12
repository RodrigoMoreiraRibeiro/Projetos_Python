from random import randint
'''maquina = 0

count = 0
tentativas = 0

while tentativas < 101:
    n1 = int(input('Tente advinhar o número da máquina: '))
    n = randint(1, 10)
    tentativas += 1
    if n == n1:
        count += 1
        break
    elif n != n1:
        print(f'A maquina escolheu o número {n} e você escolheu o numero {n1}, por tanto você perdeu!')
        print('Tente novamente')

print(f' A maquina escolheu o número {n} e você escolheu o numero {n1}, por tanto você acertou!')
print(f'Voce tentou {tentativas} vezes para ganhar da máquina')'''

# Solução Curso em Video

computador = randint(0, 10)
print('Sou seu computador, tente acertar o número que pensei')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual é seu palpite?  '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... Tente mais uma vez.')
        elif jogador > computador:
            print('Menos... Tente mais uma vez.')
print(f'Acertou com {palpites} tentativas')





