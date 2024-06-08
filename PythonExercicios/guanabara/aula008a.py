import math
num=int(input('Digite um número '))
raiz=math.sqrt(num)
print(f'A raíz de {num} é igual a {raiz:.2f}.')
print(f'Raíz arredondada para cima {math.ceil(raiz):.2f}')
print(f'Raíz arredondada para baixo {math.floor(raiz):.2f}.')

#preciso do meu import math no começo pra poder especificar

import random
dado=random.randint(1,4)
aluno=random.choice(4)#precisa fazer o nome aparecer e na ordem
print(f'\nO aluno {dado} foi escolhido para apagar o quadro e apresentarão o trabalho na ordem {aluno}')

import emoji
print(emoji.emojize('Undertale :heart:', language='alias'))

num2=float(input('Digite um número '))
print(f'O número real  do número {num2} é {math.trunc(num2)}.')

num3=float(input('Digite o comprimento do cateto oposto (em centímetros) '))
raiz3=math.sqrt(num3)
num4=float(input('Digite o comprimento do cateto adjacente (em centímetros) '))
raiz4=math.sqrt(num4)
hip=math.pow(raiz3+raiz4,2)
print(f'A hipotenusa desse triângulo retângulo é igual a {hip}cm.') #nao está funcionando como o esperado.

ang=float(input('Digite um ângulo '))
sen=math.sin(ang)
cos=math.cos(ang)
tg=math.tan(ang)
print(f'Possui {sen} de seno, {cos} de cosseno e {tg} de tangente.')