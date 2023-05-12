primeiro = int(input("Primeiro elemento: "))
razao = int(input("Razao: "))


var = primeiro
cont = 1

while cont <= 10:
    print(f'{var} -> ', end='')
    var = var + razao
    cont += 1
print('FIM')