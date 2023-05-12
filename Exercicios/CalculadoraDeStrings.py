nome = input('Digite seu nome: ')
print('Seu nome em letras maiusculas: ', nome.upper())
print('Seu nome em letras minusculas: ', nome.lower())
print('Seu nome tem o total de ', len(nome.replace(' ', '')))
dividido = nome.split()
print('Seu primeiro nome tem: ', len(dividido[0]))


