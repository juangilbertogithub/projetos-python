lista=[]
for c in range (1,6):
    peso=float(input('Digite seu peso: '))
    lista+=[peso]

print(f'O maior peso da lista é {max(lista)}kg e o menor é {min(lista)}kg.')