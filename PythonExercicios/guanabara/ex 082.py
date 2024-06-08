resp='S'
lista=[]
listapar=[]
listaimpar=[]

while resp == 'S':
    num = int(input('Insira um valor: '))
    lista.append(num)

    resp = str(input('Deseja continuar? [Sim/Não]: ')).strip().upper()[0]

    if resp == 'N':
        break

    if resp != 'S':
        print('Esse valor não existe. Por favor, tente novamente')

for p,c in enumerate(lista):
    if c%2==0
        listapar.append(c)
    elif c%2==1:
        listaimpar.append(c)

print(lista)
print(listapar)
print(listaimpar)
