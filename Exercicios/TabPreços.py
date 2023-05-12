prod = ('Lapis', 1.75, 'Borracha', 2, 'Caderno', 15.9, 'Estojo', 25, 'Transferidor',
        4.2, 'Compasso', 9.99, 'Mochila', 120.32, 'Canetas', 22.3, 'Livro', 34.90)
print('_'*50)
print(f'LISTAGEM DE PREÇOS'.center(45))
print('_'*50)

'''print(f'{prod[0]:.<40}', f'R$ {prod[1]:.2f}')
print(f'{prod[2]:.<40}', f'R$ {prod[3]:.2f}')
print(f'{prod[4]:.<40}', f'R$ {prod[5]:.2f}')
print(f'{prod[6]:.<40}', f'R$ {prod[7]:.2f}')
print(f'{prod[8]:.<40}', f'R$ {prod[9]:.2f}')
print(f'{prod[10]:.<40}', f'R$ {prod[11]:.2f}')
print(f'{prod[12]:.<40}', f'R$ {prod[13]:.2f}')
print(f'{prod[14]:.<40}', f'R$ {prod[15]:.2f}')
print(f'{prod[16]:.<40}', f'R$ {prod[17]:.2f}')'''

for pos in range(0, len(prod)):
        if pos % 2 == 0:
                print(f'{prod[pos]:.<40}', end='')
        else:
                print(f'R${prod[pos]:>7.2f}')










