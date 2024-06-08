a=float(input('Insira o valor do primeiro lado: '))
b=float(input('Insira o valor do segundo lado: '))
c=float(input('Insira o valor do terceiro lado: '))
if a<b+c and b<a+c and c<a+b:
    print('É possível formar um triângulo.')
    if a==b and b==c: #and c==a: #a==b==c
        print('Seu triângulo é equilátero.')
    elif a==b or b==c or c==a:
        print('O seu triângulo é isósceles')
    elif a!=b!=c!=a: #cuidado com a diferença. n é como a igualdade.
        print('O seu triângulo é escaleno')
else:
    print('Não é possível formar um triângulo.')