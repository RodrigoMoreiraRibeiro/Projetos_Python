import random
a1 = input('Digite o Aluno 1: ')
a2 = input('Digite o Aluno 2: ')
a3 = input('Digite o Aluno 3: ')
a4 = input('Digite o Aluno 4: ')
lista = [a1, a2, a3, a4]
random.shuffle(lista)
print('Os alunos serão sorteados na seguinte orden')
print(lista)


