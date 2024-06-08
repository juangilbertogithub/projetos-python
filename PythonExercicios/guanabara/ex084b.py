pessoas=list()
dados=list()
contagem=0
maior=menor=0

while True:
    nome=str(input('Digite o nome: ')).strip().capitalize()
    dados.append(nome)
    peso=int(input('Digite o peso: '))
    dados.append(peso)

    """if contagem == 0:
        maior=menor=peso
    else:
        if peso > maior:
            maior=peso
        if peso < menor:
            menor=peso"""

    if len(pessoas)==0:
        maior=menor=dados[1]
    else:
        if dados[1] > maior:
            maior=dados[1]
        if dados[1]< menor:
            menor=dados[1]

    pessoas.append(dados[:])
    dados.clear()

    contagem += 1

    pergunta=str(input('Deseja continuar? Sim ou Não: ')).strip().upper()[0]
    if pergunta == 'N':
        break

print(f'Você cadastrou {contagem} pessoas.', pessoas) #ou poderia por apenas len(pessoas)

"""print(f'O maior peso foi: {maior}kg. É o peso de ',end='')
for p,v in enumerate(pessoas):
    if pessoas[p][1] == maior:
        print(f'{pessoas[p][0]}', end=' ')
print()

print(f'O menor peso foi: {menor}kg. É o peso de ',end='')
for p,v in enumerate(pessoas):
    if pessoas[p][1] == menor:
        print(f'{pessoas[p][0]}', end=' ')
print()"""

print(f'O maior peso foi: {maior}kg. É o peso de ',end='')
for p in pessoas:
    if p[1] == maior:
        print(p[0], end=' ')
print()

print(f'O menor peso foi: {menor}kg. É o peso de ',end='')
for p in pessoas:
    if p [1] == menor:
        print(p[0], end=' ')
print()