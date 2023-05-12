fr = str(input('Digite uma frase: ')).upper().strip()
print('A letra A aparece {} vezes na frase'.format(fr.count('A')))
print('A letra A aparece a primeira vez na posição {}ª'.format(fr.find('A') + 1))
print('A letra A aparece a uiltima vez na posição {}º'.format(fr.rfind('A') + 1))


