listacompleta=list()
lista=list()
listapar=list()
listaimpar=list()

for c in range (1,8):
    numero=int(input(f'Digite um número ({c}/7): '))
    lista.append(numero)
    if numero%2==0:
        listapar.append(numero)
    if numero%2==1:
        listaimpar.append(numero)

lista.sort()
listapar.sort()
listaimpar.sort()

listacompleta.append(lista),listacompleta.append(listapar), listacompleta.append(listaimpar)
print(f"""Lista completa: {listacompleta[0]}
Lista par: {listacompleta[1]}
Lista ímpar: {listacompleta[2]}""")

#OU

numeros=[[],[]]
valor=0
for c in range (1,8):
    valor=int(input(f'Digite um valor ({c}/7): '))
    if valor%2==0:
        numeros[0].append(valor)
    else:
        numeros[1].append(valor)
numeros[0].sort() #sorteia apenas aquela parte espepcifica da lista. NAO SABIA
numeros[1].sort()
print(f"""Todos os valores: {numeros}
Valores pares: {numeros[0]}
Valores ímpares: {numeros[1]}""")