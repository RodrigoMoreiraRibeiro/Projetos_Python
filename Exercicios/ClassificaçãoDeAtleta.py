from datetime import date
dataAtual = date.today()
dn = int(input('Ano de nascimento: '))
dc = dataAtual.year
idade = dc - dn
print(f'Sua idade é {idade}')


if idade <= 9:
    print('Classificação: Mirim')
elif idade <= 14:
    print('Classificação: Infantil')
elif idade <= 19:
    print('Classificação: Junior')
elif idade <= 25:
    print('Classificação: Sênior')
elif idade > 25:
    print('Classificação: Master')
