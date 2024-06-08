"""from math import factorial
n=int(input('Insira um fatorial: '))
f=factorial(n)
print(f'O fatorial de {n} é {f}')"""

"""n=int(input('Insira um fatorial: '))
f=1

print(f'Fatorial de {n}!')
for c in range (n, 0, -1):
    f=f*c
    print(f'{c}', end='')
    print(' x ' if c > 1 else ' = ', end='')
print(f)"""

n=int(input('Insira um fatorial: '))
f=1

print(f'Fatorial de {n}!')
while n>0:
    print(f'{n}', end='') #tem q colocar esse print em cima se n ele vai do n-1 ate o 0, que seria o errado
    print(' x ' if n>1 else ' = ', end='') #uso interessante do if e else
    f *= n #o f tem q ser em cima, pq se tiver embaixo aparece o 0 e da problema no meu calculo
    n-=1
print(f)