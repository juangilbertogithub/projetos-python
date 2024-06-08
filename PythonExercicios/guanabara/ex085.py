listapar=[]
listaimpar=[]

for c in range (1,8):
    num=int(input('Insira um número: '))
    if num%2==0:
        listapar.append(num)
    else:
        listaimpar.append(num)

listapar.sort()
listaimpar.sort()

print(listapar)
print(listaimpar)