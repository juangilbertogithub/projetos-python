n1=int(input('Insira um número: '))
n2=int(input('Insira um número: '))
n3=int(input('Insira um número: '))
n4=int(input('Insira um número: '))

lista=(n1,n2,n3,n4)

print(f'O número 9 apareceu {lista.count(9)} vezes.')
print(f'A posição do primeiro número 3 foi em {lista.index(3) + 1}.')
print(f'Os números pares são: ', end='')
for numero in lista:
    if numero%2==0:
        print(numero, end=' ')


#n faço dieia de como fazer a parte do par