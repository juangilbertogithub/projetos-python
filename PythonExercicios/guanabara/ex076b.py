listagem=('A', 1, 'B', 2, 'C', 3)

print('-'*40)
print(f'{"LISTAGEM DE PREÇO":^40}')
print('-'*40)

for c in range (0,len(listagem)):

    if c % 2 == 0:
        print(f'{listagem:.<30}', end=" ")
    else:
        print(f'R${listagem:>7.2f}')

print('-'*40)