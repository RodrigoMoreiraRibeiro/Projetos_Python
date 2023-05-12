quant = tot = prod = b = cont = maior = menor = 0

while True:
    produto = str(input('Digite o nome do produto: ')).strip().upper()
    valor = float(input('Digite o valor do produto R$'))
    tot += valor
    quant += 1

    if valor > 1000:
        prod = prod + 1

    if quant == 1 or valor < menor:
        menor = valor
        menor_prod = produto
    #else:
     #   if valor < menor:
      #      menor = valor
       #     menor_prod = produto

    rsp = str(input('Deseja continuar? [S/N] :')).strip().upper()[0]

    if rsp == 'S':
        continue
    if rsp == 'N':
        break


print(f'A soma total de foi R${tot:.2f} E Teve {prod} produtos acima de R$1000.00')
print(f'E o produto mais barato foi o {menor_prod}')













