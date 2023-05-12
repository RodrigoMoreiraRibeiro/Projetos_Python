from datetime import date
dataAtual = date.today().year
totmaior = 0
totmenor = 0
for pessoa in range(1, 8):
    dn = int(input(f'Em que ano a {pessoa}º pessoa nasceu? : '))
    idade = dataAtual - dn
    if idade >= 21:

        totmaior += 1
    else:
        totmenor += 1

print(f'Ao todo tivemos {totmaior} pessoas maiores de idade')
print(f'E também tivemos {totmenor} pessoas menores de idade')
