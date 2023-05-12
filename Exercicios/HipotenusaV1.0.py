import math
cateto1 = float(input('Digite o cateto1: '))
cateto2 = float(input('Digite o cateto2: '))
#hipotenusa = math.sqrt(cateto1**2 + cateto2**2)


#método do cursoemvidedo
hipotenusa = math.hypot(cateto1, cateto2)

#método sem o math
#hipotenusa = (cateto1 ** 2 + cateto2 ** 2) ** (1/2)

print(f'Os catetos são {cateto1} e {cateto2} e a hipotenusa é {hipotenusa:.2f}')


