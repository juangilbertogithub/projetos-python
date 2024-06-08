dados=list()
dados.append('Pedro')
dados.append(25)
print(dados[0])
print(dados[1])

pessoas=list()
pessoas.append(dados[:]) #copia dos dados e insiro dentro da lista.
print(pessoas)

dados2=list()
dados.append('Maria')
dados.append(19)

dados3=list()
dados.append('João')
dados.append(32)

"""pessoas2=list()
pessoas2.append(dados[:]),pessoas2.append(dados2[:]),pessoas2.append(dados3[:])
print(pessoas2)""" #da um erro estranho

pessoas=[['Pedro',25],['Maria',19],['João',32]]
print(pessoas)
print(pessoas[0][0])
print(pessoas[1][1])
print(pessoas[2][0])
print(pessoas[1])
for p in pessoas:
    print(f'Dado geral: {p} \nApenas nome: {p[0]} \nApenas idade: {p[1]}')

"""pessoasteste=list()
pessoasteste.append(pessoas)
pessoasteste[0]=['Marco',26]
print(pessoasteste[0])"""  #funciona meio esquisito

galera=list()
dados=list()
menor=maior=0
for c in range (0,3):
    dados.append(str(input('Insira o nome: ')))
    dados.append(int(input('Insira a idade: ')))
    galera.append(dados[:]) #se n for uma copia, irão aparecer espaços vazios
    dados.clear()
print(galera)

for p in galera:
    if p[1] >=18:
        print(f'O {p[0]} é maior de idade.')
        maior+=1
    else:
        print(f'O {p[0]} é menor de idade')
        menor+=1

print(f'Existe um total de {maior} pessoas maiores de idade.')
print(f'Existe um total de {menor} pessoas menores de idade.')