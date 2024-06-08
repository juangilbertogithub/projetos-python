n1=int(input('Digite o primeiro número: '))
n2=int(input('Digite o segundo número: '))
lista=(n1,n2)
print(f'O maior número digitado foi o {max(lista)}. O quadrado desse valor é {max(lista)**2}.')

#outra maneira

n1=int(input('Digite o primeiro número: '))
n2=int(input('Digite o segundo número: '))
if n1>n2:
    print(f'O maior número digitado foi o {n1}. O quadrado desse valor é {n1**2}.')
if n2>n1:
    print(f'O maior número digitado foi o {n2}. O quadrado desse valor é {n2**2}.')

#Escreva um programa em Python que leia dois números distintos e apresente o quadrado do maior número.