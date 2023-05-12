vel = float(input('A velocidade que o carro passou foi: '))

if vel > int(80):
    m = vel-int(80)
    v = int(7)*m
    print('O carro ultrapassou o limite de velocidade e a multa é de R${:.2f}'.format(v))
else:
    print('Tenha um bom dia, e dirija com segurança! ')