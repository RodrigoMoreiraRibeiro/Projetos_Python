sal = float(input('Digite seu salário: R$'))

aumento1 = sal * 0.10 + sal
aumento2 = sal * 0.15 + sal

if sal > float(1250.00):
    print('O seu salário é de R${:.2f} com o aumento de 10%'.format(aumento1))
else:
    print('O seu salário será R${:.2f} com o aumento de 15%'.format(aumento2))
