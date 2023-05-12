from datetime import date
dataAtual = date.today().year
dn = int(input('Ano de nascimento: '))
idade = dataAtual - dn
print(f'Sua idade é {idade} Anos')


if idade < 18:
    falta = 18 - idade
    print(f'Ainda não está na hora de se alistar!!!, Faltam {falta} Ano(s)')
elif idade == 18:
    print('Está na hora de se alistar!!!')
elif idade > 18:
    passou = idade - 18
    print(f'Ja passou da hora de se alistar!!!, Passou {passou} Ano(s)')