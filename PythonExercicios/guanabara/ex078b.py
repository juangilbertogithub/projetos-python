lista=[]

for c in range (0,5):
    """num = int(input('Insira um valor: '))
    lista.append(num)"""
    lista.append(int(input(f'Insira um valor para a posição {c+1}: ')))

print(f'O valor mínimo inserido foi o {min(lista)}. Está na posição: ', end='')
for c,v in enumerate(lista):
    if v == min(lista):
        print(c+1, end= ' ')
print()

print(f'O valor máximo inserido foi o {max(lista)}. Está na posição: ', end='') #{lista.index(max(lista))+1}
for c,v in enumerate(lista):
    if v == max(lista):
        print(c+1, end= ' ')
print()

