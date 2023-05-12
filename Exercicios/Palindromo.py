frase = str(input('Digite uma frase: ')).replace(' ', '').upper()

frase2 = frase[::-1]


if frase == frase2:
    print(f'A frase  {frase} {frase2} É um polindromo!')
else:
    print(f'A palvra {frase} {frase2} Não é um palindromo')

