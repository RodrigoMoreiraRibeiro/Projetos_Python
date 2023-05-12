
'''while True:
    lista = ('Somar', 'Multi', 'Maiorr', 'Novos Numeros', 'Sair')
    n1 = int(input('Digite um valor: '))
    n2 = int(input('Digite outro valor: '))

    rspt = str(input(''
                     '\n [0] SOMAR\n'
                     '\n [1] MULTIPLICAR\n'
                     '\n [2] MAIOR\n'
                     '\n [3] NOVOS NÚMEROS\n'
                     '\n [4] SAIR\n'
                     '\nEscolha uma das opções: '))


    if rspt == '0':
        soma = n1 + n2
        print(f'A soma dos valores {n1} + {n2} é = {soma}')

    elif rspt == '1':
        mult = n1 * n2
        print(mult)

    elif rspt == '2':
        if n1 > n2:
            print(f'O maior número é o {n1}')
        else:
            print(f'O maior número é o {n2}')

    elif rspt == '3':
        print('Digite novos numeros\n')
        continue

    elif rspt == '4':
        print('Voce saiu do Programa!!!')
        break

    else:
        print('Resposta inválida!')'''

# Solução Curso em Video
from time import sleep
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
opcao = 0
while opcao != 5:
    print('''    [1] SOMAR
    [2] MULTIPLICAR
    [3] MAIOR
    [4] NOVOS NÚMEROS
    [5] SAIR''')
    rspt = int(input('Qual é a sua opção? '))
    if rspt == 1:
        soma = n1 + n2
        print(f'A soma dos valores {n1} + {n2} é = {soma}')

    elif rspt == 2:
        mult = n1 * n2
        print(f'A multiplicçao dos valores {n1} * {n2} é = {mult}')

    elif rspt == 3:
        if n1 > n2:
            print(f'O maior número entre {n1} e {n2} é o {n1}')
        else:
            print(f'O maior número entre {n1} e {n2} é o {n2}')

    elif rspt == 4:
        print('Digite novos numeros\n')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))


    elif rspt == 5:
        break

    else:
        print('Resposta inválida!')
    sleep(2)
print('Fim do programa!')




