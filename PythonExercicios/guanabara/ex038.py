"""n1=int(input('Digite um número inteiro: '))
n2=int(input('Digite outro número inteiro: '))
lista=[n1,n2]

if n1!=n2:
    print(f'{max(lista)} é o maior número.')
    print(f'{min(lista)} é o menor número.')

if n1==n2:
    print(f'Não existe um valor maior. Ambos são iguais.')"""

"""n1=int(input('Digite um número inteiro: '))
n2=int(input('Digite outro número inteiro: '))

if n1!=n2:
    maior=n1
    if n2>n1:
        maior=n2

    print(f'O maior é {maior}.')

    menor=n1
    if n2<n1:
        menor=n2

    print(f'O menor é {menor}.')

if n1==n2:
    print('Não existe valor maior ou menor. Os números são iguais.')"""

n1=int(input('Digite um número inteiro: '))
n2=int(input('Digite outro número inteiro: '))

if n1>n2:
    print('O PRIMEIRO é MAIOR.')
elif n2>n1:
    print('O SEGUNDO é MAIOR.')
elif n1==n2:
    print('Os dois são iguais.')