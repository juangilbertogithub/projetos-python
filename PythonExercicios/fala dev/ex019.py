print('Calculadora de função do 2º grau.')
a=int(input('Insira o valor de A: '))
b=int(input('Insira o valor de B: '))
c=int(input('Insira o valor de C: '))
delta=(b**2-4*a*c)**(1/2)
if delta<0:
    print('A raíz não é real.')
elif delta==0:
    raiz = -b / (2 * a)
    print(f'Como delta é 0, só possuirá uma raíz: {raiz:.0f}.')

elif delta > 0:
    raiz1 = (-b + delta) / (2 * a)
    raiz2 = (-b - delta) / (2 * a)
    print(f'Como delta é maior que 0, possuirá duas raízes: {raiz1:.0f} e {raiz2:.0f}.')



#Escreva um programa que faz a leitura de três valores reais (A, B e C),representando os coeficientes de uma equação do
#2o. grau, calcula o valor do delta e os valores das raízes reais, caso existam.