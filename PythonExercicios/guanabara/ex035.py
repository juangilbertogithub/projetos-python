from time import sleep
print('=-'*20)
print('Analisando um triângulo')
print('=-'*20)
sleep(1)
a=float(input('Insira o valor do primeiro lado: '))
b=float(input('Insira o valor do segundo lado: '))
c=float(input('Insira o valor do terceiro lado: '))
if b-c<a<b+c:
    print('É possível formar um triângulo.')
#if a<b+c and b<a+c and c<a+b
else:
    print('Não é possível formar um triângulo.')