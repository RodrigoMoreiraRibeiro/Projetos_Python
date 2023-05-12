primeiro = int(input("Primeiro elemento: "))
razao = int(input("Razao: "))
n = int(input("Quantos elementos exibir: "))

var = primeiro
count = 0

while count < n:
    print(f'{var} -> ', end='')
    var = var + razao
    count = count + 1
print('PAUSA')
rst = str(input('Deseja continuar? [S/N]')).upper()
tot = 0
while rst == 'S':
    mais_n = int(input('Quantos elementos exibir: '))
    count = 0
    while count < mais_n:
        var = var + razao
        count = count + 1
    count = 0
    while count < mais_n:
        print(f'{var} -> ', end='')
        var = var + razao
        count = count + 1
    print('PAUSA')
    rst = str(input('\nDeseja continuar? [S/N]')).upper()

print('Fim')
print(f'Foram exibidos {tot} termos')

