pp = float(input('Digite o preço do produto R$:'))
print('[1] Á vista dinheiro')
print('[2] Á vista no cartão')
print('[3] 2x no cartão')
print('[4] 3x ou mais no cartão')

pgmt = str(input('Escolha a forma de pagamento: '))

if pgmt == '1':
    desc1 = float(pp - pp * 0.10)
    print(f'O valor á vista ficou R${desc1:.2f} com 10% de desconto')
elif pgmt == '2':
    desc2 = float(pp - pp * 0.05)
    print(f'O valor á vista no cartão ficou R${desc2:.2f} com 5% de desconto')
elif pgmt == '3':
    normal = float(pp)
    print(f'O valor parcelado em 2x ficou R${normal:.2f} sem juros')
elif pgmt == '4':
    pgt1 = int(input('Em quantas vezes será?'))
    juros = float(pp + pp * 0.20)
    parcela = juros / pgt1
    print(f'O valor parcelado em {pgt1}x de {parcela} ficou  R${juros:.2f} com juros de 20%')
else:
    print('Opção inválida')
