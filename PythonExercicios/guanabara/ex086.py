"""matriz=[[0,0,0],[0,0,0],[0,0,0]]

for l in range (1,4):
    for c in range (1,4):
        matriz.append(int(input('Insira um valor: '))) #tem como fazer sem append colocando os 0

for l in range (0,3):
    for c in range (0,3): #atençao nos valores colocados no range
        matriz [l][c] = int(input('Insira um valor: '))

print(matriz)

for l in range (0,3):
    for c in range (0,3):
        print(f'{matriz[l][c]:^5}', end='')
    print()"""


matriz=[[],[],[]]
for l in range (0,3):
    for c in range (0,3):
        matriz[l].append(int(input(f'Insira um valor ({l},{c}): ')))

for l in range (0,3):
    for c in range (0,3):
        print(f'{matriz[l][c]:^5}', end='') #nao esquecer que o lance dos espaços é sempre dendro do parenteses pra dar certo
    print()