n1=int(input('Digite o primeiro número: '))
n2=int(input('Digite o segundo número: '))
if n1>n2:
    print(f'{n1} é maior.')
elif n2>n1:
    print(f'{n2} é maior.')
elif n2 == n1:
    print(f'{n1} e {n2} são iguais.')

"""lista=(n1,n2)
maior=n1
if n2>n1:
    maior=n2
    print(f'O número {n2} é o maior')
elif n2==n1:
    print(f'Os valores são iguais ({n2}), logo, não há um maior.')
else:
    print(f'O número {n1} é maior.')"""