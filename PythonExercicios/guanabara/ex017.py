'''from math import sqrt
co=float(input('Comprimento do cateto oposto: '))
ca=float(input('Comprimento do cateto adjacete: '))
hi=(co**2)+(ca**2)
hi2=sqrt(hi)
print(f'A hipotenusa é igual a {hi2:.2f}.')'''

'''co=float(input('Comprimento do cateto oposto: '))
ca=float(input('Comprimento do cateto adjacete: '))
hi=(co**2)+(ca**2)
hi2=hi**1/2
print(f'A hipotenusa é igual a {hi2:.2f}.')'''

import math
co=float(input('Comprimento do cateto oposto: '))
ca=float(input('Comprimento do cateto adjacete: '))
hi=math.hypot(co,ca)
print(f'A hipotenusa é igual a {hi:.2f}.')