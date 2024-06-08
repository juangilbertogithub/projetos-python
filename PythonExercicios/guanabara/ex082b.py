lista=[]
listapar=[]
listaimpar=[]

while True:
    lista.append(int(input('Insira um número: ')))

    pergunta=str(input('Deseja continuar? Sim ou Não: ')).strip().upper()[0]
    if pergunta == 'N':
        break

lista.sort()

for c in lista:
    if c%2==0:
        listapar.append(c)
    if c%2==1:
        listaimpar.append(c)


print(f'A lista (em ordem) completa é {lista}.')
print(f'A lista somente com os pares é {listapar}.')
print(f'A lista apenas com os ímpares é {listaimpar}.')
