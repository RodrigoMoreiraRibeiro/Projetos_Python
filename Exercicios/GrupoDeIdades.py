somaidade = mediaidade = maioridadehomem = nomevelho = totmulher20 = 0

for p in range(1, 5):
    print(F'----- {p}º PESSOA -----')
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().upper()
    somaidade += idade
    if p == 1 and sexo in 'M':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'M' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'F' and idade < 20:
        totmulher20 += 1
mediaidade = somaidade / p
print(f'A media da idade do Grupo é de {mediaidade} anos')
print(f'O homem nome mais velho é {nomevelho} e ele tem {maioridadehomem}')
print(f'Ao todo são {totmulher20} mulheres com menos de 20 anos')
