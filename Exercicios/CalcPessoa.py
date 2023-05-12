cont1 = cont2 = cont3 = 0
while True:
    idade = int(input('Qual a sua idade? '))
    sexo = str(input('Qual o seu Sexo? [F/M] ')).strip().upper()[0]


    if sexo != 'F' and sexo != 'M':
        print('Opção inválida')

    if idade > 18:
        cont1 += 1
        mais18 = cont1

    if sexo == 'M':
        cont2 += 1
        qntdH = cont2

    if sexo == 'F' and idade > 20:
            cont3 += 1

    rsp = str(input('Deseja continua? [S/N]')).strip().upper()

    if rsp != 'S' and rsp != 'N':
        print('OPÇÃO INVÁLIDA, TENTE NOVAMENTE!')
        continue

    if rsp == 'S':
        continue

    else:
        print('Voce saiu')
        break

print(f'Foram cadastradas {cont1} pessoa(s) acima de 18 anos')
print(f'Sendo {cont2} Homen(s)')
print(f'E possuindo {cont3} Mulher(es) acima de 20 anos')

