
'''n = 0
soma = 0
media = 0
maior = 0
menor = 0

while True:

    n = int(input('Digite um numero: '))
    rsp = str(input('Quer continuar? [S/N]')).upper()
    soma = soma + n
    media += 1

    if rsp == 'S':
        continue

    if rsp == 'N':
        print(soma/media)

        break

    else:
        print('Inválido')
        continue'''

# Solução Curso em video completa

resp = 'S'
soma = quant = media = maior = menor = 0
while resp in 'Ss':
    num = int(input('Digite um número: '))
    soma += num
    quant += 1
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num


    resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
media = soma / quant
print(f'Voce digitou {quant} numeros e a média foi {media}')
print(f'O maior valor foi {maior} e o menor foi {menor}')








