primeiro = int(input("Primeiro elemento: "))
razao = int(input("Razão: "))
n = int(input("Quantos elementos exibir: "))

ultimo = primeiro + (n-1)*razao

var = primeiro
cont = 0

while var <= ultimo:
    print(var)
    var += razao
    cont += 1

    if cont == n:
        rst = input('Deseja continuar? [S/N]').upper()

        if rst == 'S':
            n = int(input("Quantos elementos exibir: "))
            ultimo = var + (n-1)*razao - razao
            cont = 0

print('Fim do Programa')
