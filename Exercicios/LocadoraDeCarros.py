km = float(input('Quantos km rodados?: '))
dia = int(input('Quantos dias usado?: '))
vdia = dia * 60
vkm = km * 0.15

print('O carro percorreu {:.3f}km e {} dias e o valor total a ser pago de RS${:.2f}'.format(km, dia, vdia + vkm))
