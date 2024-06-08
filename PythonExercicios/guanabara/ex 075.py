"""num=(int(input('Digite um número: ')),
     int(input('Digite outro número: ')),
     int(input('Digite mais um número: ')),
     int(input('Digite o último número: ')))"""

n1=int(input('Digite um valor: '))
n2=int(input('Digite um valor: '))
n3=int(input('Digite um valor: '))
n4=int(input('Digite um valor: '))

lista=(n1, n2, n3, n4)

print(f'Você digitou os números {lista}')
if 9 in lista:
    print(f'O valor nove apareceu {lista.count(9)}.')
else:
    print('Não possui o valor 9 na lista.')
if 3 in lista:
    print(f'O valor 3 apareceu na posição {lista.index(3)+1} pela primeira vez.')
else:
    print('Não possui o valor 3 na lista.')

print('Os valores pares digitados foram ',end='')
for n in lista:
    if n%2==0:
        print(n, end=' ')

"""valores = tuple(int(input('Digite valores '))for c in range(1, 5))
print(f'O numero nove aparece {valores.count(9)} vezes')
print(f'Valor 3 foi digitado pela primeira vez na {valores.index(3)+1}º posição' if 3 in valores else 'Não foi digitado valor 3')
print('Valores pares digitados foram', end=' ')
print({n for n in valores if n % 2 == 0}, end=' ')"""