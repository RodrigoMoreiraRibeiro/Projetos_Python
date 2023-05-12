km = int(input('Digite a distancia da viagem: '))
b = float(0.50)
c = float(0.45)
print('Você está prestes a fazer uma viagem de {}km'.format(km))

if km >= 200:
    cr = km * c
    print('O valor da viagem ficou em R${:.2f}'.format(cr))
else:
    br = km * b
    print('O valor da viagem ficou em R${:.2f}'.format(br))

