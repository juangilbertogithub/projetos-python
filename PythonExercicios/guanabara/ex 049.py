n=int(input('Digite um número: '))

print(f'\nA taubada de {n} é\n')
print('=' * 15)

for c in range (0,n+1):
    print(f'{n} x {c} = {n * c:3}')
print('=' * 15)