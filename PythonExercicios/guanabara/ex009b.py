n=int(input('Digite um número: '))

print(f'Tabuada de {n}')

for c in range (0,11):
    print(f'{n} x {c:2} = {n*c}') # :2 indica que quero 2 espaços