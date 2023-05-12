times = ('Corinthians', 'Palmeiras', 'Santos', 'Grêmio', 'Cruzeiro', 'Flamengo', 'Vasco da Gama', 'Chapecoense',
'Atlético-MG', 'Botafogo', 'Athletico-PR', 'Bahia', 'São Paulo',
'Fluminense', 'Sport Recife', 'EC Vitória', 'Coritiba', 'Avaí', 'Ponte Preta', 'Atletico-GO')
print('='*40)
print('        TABELA BRASILEIRÃO 2017')
print('='*40)


print('Os 5 Primeiros são')
for cont in range(0, len(times[:5])):

    print(f'{cont+1}º {times[cont]}')
print('='*40)
print('Os 4 ultimos colocados São')
for cont in range(16, len(times[:20])):

    print(f'{cont+1}º {times[cont]}')
print('='*40)
print('Os Time em ordem Alfabética')

print(sorted(times))
print('='*40)
for cont in range(7, len(times[5])):

    print(f'O time {times[7]} está em {cont+1}º posição ')








