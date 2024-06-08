lista=[]
#listamulheres=[]
dados={}
idade=0
while True:
    dados['nome']=str(input('Nome: ')).strip().capitalize()
    dados['idade']=int(input('Idade: '))

    while True:
        dados['sexo'] = str(input('Sexo [M/F]: ')).strip().upper()[0]
        if dados['sexo'] in 'MF':
            break
        print('Erro. Por favor, digite M ou F.')

    #print(dados)
    lista.append(dados.copy())
    #del dados['nome'], dados['idade'], dados['sexo']  ou dados.clear() nao precisa pq dicionario pode sobrepor

    while True:
        pergunta = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
        if pergunta in 'SN':
            break
        print('Erro. Por favor, digite S ou N.')
    if pergunta == 'N':
        break

#print(lista)
if len(lista)==1:
    print(f'{len(lista)} pessoa cadastrada.')
else:
    print(f'{len(lista)} pessoas cadastradas.')

for k,v in enumerate(lista):
    idade+=v['idade']
idademedia=int(idade/len(lista))
print(f'A média das idades é de {idademedia}.')

print('As mulheres na lista são: ',end='')
for k,v in enumerate(lista):
    if v['sexo']=='F':
        print(f'{v["nome"]}', end= ' ')
print()

"""        listamulheres.append(v)
print('Lista apenas com as mulheres:')
for c in listamulheres:
    print(c)"""

print(f'Lista de pessoas acima da média são: ', end='')
for k,v in enumerate(lista):
    if v['idade'] > idademedia:
        print(f'{v["nome"]}', end=' ')
print()