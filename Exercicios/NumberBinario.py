numero = int(input('Digite um número: '))
print('[1] BINÁRIO')
print('[2] OCTAL')
print('[3] HEXADEDCIMAL')

prgt = str(input('Selecione a opção deseja: ')).upper()


if prgt == '1':
    b = str(bin(numero)[2:])
    print(b)
elif prgt == '2':
    o = str(oct(numero)[2:])
    print(o)
elif prgt == '3':
    h = str(hex(numero)[2:])
    print(h)
else:
    print('Opção inválida!!!')
