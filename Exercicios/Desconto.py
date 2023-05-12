p = float(input('Digite o preço: R$'))
desc = p * 0.05


print('O valor de R${:.2f} irá para R${:.2f} com desconto de 5%'.format(p, p - desc))
