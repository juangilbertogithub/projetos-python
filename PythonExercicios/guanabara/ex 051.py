a=int(input('Escolha o primeiro termo: '))
r=int(input('Escolha uma razão: '))
n= a+(10)*r
for c in range(a,n,r):
    print(f'{c}', end=' > ')
print('FIM')