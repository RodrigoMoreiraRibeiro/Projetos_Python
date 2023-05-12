n1 = float(input('Digite a nota 1: '))
n2 = float(input('Digite a nota 2: '))

m = (n1 + n2) / 2

if m < 5.0:
    print(f'Reprovado com a média de {m:.1f}')
elif m >= 5.0 and m < 7.0:
    print(f'Recuperação com a média de {m:.1f}')
elif m >= 7.0:
    print(f'Aprovado!!! com a média de {m:.1f}')

