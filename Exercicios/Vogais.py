palavras = ('APRENDER','PROGRAMAR', 'LINGUAGEM', 'PYTHON', 'CURSO', 'GRATIS',
            'ESTUDAR', 'PRATICAR', 'TRABALHAR', 'MERCADO', 'PROGRAMADOR', 'FUTURO')
vogais = 'aeiouAEIOU'

for palavra in palavras:
    print(f'Vogais em {palavra}:', end=' ')
    for letra in palavra:
        if letra in vogais:
            print(letra, end=' ')
    print('')