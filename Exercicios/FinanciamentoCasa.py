vc = float(input('Digite o valor ca casa R$:'))
sal = float(input('Digite o seu sálario atual R$:'))
qa = int(input('Em quantos anos pretende pagar?'))

meses = qa * 12
vp = vc / meses

print('O valor da casa é de R${:.3f}\nO seu salário é de R${:.3f}\nPara pagar em {} anos'.format(vc,sal,qa))

if vp < sal * 0.30:
    print('Empréstimo Aprovado!,A parcela ficara em R${:.3f} durante {} meses'.format(vp, meses))

else:
    print(f'Para pagar uma casa de R${vc:.3f} em {qa} ano(s) A parcela será R${vp:.3f}')
    print('Empréstimo não Aprovado!!!')
