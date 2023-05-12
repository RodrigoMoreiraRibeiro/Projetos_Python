import random
from time import sleep
na = random.randint(0,5)

while True:
    n = int(input('Advinhe o número que a maquina imprimira: '))
    print('PROCECESSANDO...')
    sleep(2)
    if na == n:
        print('Parabéns você acertou!')
        break

    else:
        print('Não foi dessa vez, tente novamente!')
        print('A maquina pensou no número {} e vc botou o numero {}'.format(na, n))
        continue

print('A maquina pensou no número {} e vc botou o numero {}'.format(na, n))



