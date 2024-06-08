"""mais=0
total=0

while mais!=999:
    total=total+mais
    mais=int(input('Digite um número (999 para parar): '))

print(total)"""

num=0
cont=0
soma=0
num=int(input('Digite um número (999 para parar): '))
while num!=999:
    cont += 1
    soma += num
    num = int(input('Digite um número (999 para parar): '))

print(num-999, cont-1)