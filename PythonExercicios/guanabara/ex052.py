"""n=int(input('\033[1:97mDigite um número inteiro para saber se ele é ou não é primo: '))

total=0
for c in range(1, n+1):
    if n%c==0:
        print('\033[1:32m', end= ' ')
        total=total+1
        if total==2:
            primo='É'
        else:
            primo='NÃO É'
    else:
        print('\033[1:31m', end= ' ')
    print(f'{c}', end=' ')
print(f'\n\033[1:97mFoi divisível {total} vezes. Seu número {primo} primo.')"""

n=int(input('\033[1:97mDigite um número inteiro para saber se ele é ou não é primo: '))

total=0
for c in range(1    , n+1):
    if n%c==0:
        print('\033[1:32m', end= ' ')
        total=total+1
    else:
        print('\033[1:31m', end= ' ')
    print(f'{c}', end=' ')
print(f'\n\033[1:97mFoi divisível {total} vezes.')

if total == 2:
    primo = 'É'
    print('Ou seja, seu número é primo')
else:
    primo = 'NÃO É'
    print('Ou seja, seu número não é primo')
