n = ('zero', 'um', 'dois','tres','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','quatorze','quinze','dezesseis','dezessete','dezoito','dezenove',
     "vinte")

while True:
    x = int(input('Digite um numero: '))
    if x < 0 or x > 20:
        print('Número inválido, Tente novamente!')
        continue
    else:
        break

print(f'Voce digitou o número {n[x]}')














