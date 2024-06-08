valores=[]

for v in range (0,5):
    valores.append(int(input(f'Digite o valor da posição {v+1}: ')))

print(f'Os valores digitados foram: {valores}')


for p,v in enumerate(valores):
    if v==(max(valores)):
        print(f'O maior valor é {max(valores)}')
        print(f'O maior valor está na posição {p+1}')

    if v==(min(valores)):
        print(f'O menor valor é {min(valores)}')
        print(f'O menor valor está na posição {p+1}')


"""lista = []
posicao_maior = []
posicao_menor = []
for p in range(0, 5):
    val = int(input(f'Digite um valor na posição {p}: '))
    lista.append(val)
for posicao, valores in enumerate(lista):
    if valores == max(lista):
        posicao_maior.append(posicao)
    if valores == min(lista):
        posicao_menor.append(posicao)
print(f'Você digitou os valores {lista}')
print(f'O maior valor da lista é {max(lista)}, nas posições {posicao_maior}')
print(f'O menor valor da lista é {min(lista)}, nas posições {posicao_menor}')"""