num = int(input('Digite um numero de 0 a 9999: '))

unidade = num // 1 % 10
dezena = num // 10 % 10
centena = num // 100 % 10
milhar = num // 1000 % 10

print("""
    Unidade = {}
    Dezena = {}
    Centena = {}
    Milhar = {}""".format(unidade, dezena, centena, milhar))