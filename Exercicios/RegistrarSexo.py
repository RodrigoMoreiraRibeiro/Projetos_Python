'''sexo = ''
r = 'M'
r1 = 'F'


while sexo == 'M' or sexo == 'F' or sexo != 'M' and 'F':
    sexo = str(input('Qual o seu sexo? ')).upper().strip()
    if sexo == 'M':
        print('Você é do Sexo Masculino')
        break
    if sexo == 'F':
        print('Você é do Sexo Feminino')
        break
    if sexo != 'F' and sexo != 'M':
        print('Resposta Inválida')'''

# Solução Cursoemvideo

sexo = str(input('Informe seu sexo: [M/F] ')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Dados inválidos. por favor, informe seu sexo: ')).strip().upper()[0]
print(f'Sexo {sexo} registrado com sucesso!')

