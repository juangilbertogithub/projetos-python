"""maior=0
menor=0
for p in range (1, 6):
    n=int(input(f'Digite o peso da {p}ª pessoa: '))
    if p==1:
        maior=n
        menor=n
    else:
        if n > maior:
            maior=n
        if n < menor:
            menor=n

print(maior, menor)"""

lista=[] #lista vazia
for c in range (1,6):
     n=int(input('Digite seu peso: '))
     lista=lista+[n]

print(f'O maior da lista é {max(lista)} e o menor da lista é {min(lista)}.')