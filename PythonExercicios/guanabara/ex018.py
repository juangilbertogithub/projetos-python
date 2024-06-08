'''import math
ang=float(input('Digite um ângulo: ')) #quero em radiano!
sen=math.sin(math.radians(ang))
cos=math.cos(math.radians(ang))
tg=math.tan(math.radians(ang))
print(f'Do ângulo {ang}. \nO seno é {sen:.2f} \nO cosseno é {cos:.2f} \nA tangente é {tg:.2f}')'''

from math import sin,cos,tan,radians
ang=float(input('Digite um ângulo: ')) #quero em radiano!
sen=sin(radians(ang))
cos=cos(radians(ang))
tg=tan(radians(ang))
print(f'Do ângulo {ang}. \nO seno é {sen:.2f} \nO cosseno é {cos:.2f} \nA tangente é {tg:.2f}')