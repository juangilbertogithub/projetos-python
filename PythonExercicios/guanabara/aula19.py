dados=dict()
dados={'nome':'Pedro','idade':25}
print(dados['nome'])
print(dados['idade'])

dados['sexo']='M'
print(dados)

del dados['idade']
print(dados)

filme={'titulo':'Star Wars',
'ano':1977,
'diretor': 'George Lucas'
}
print(filme)
print(filme.values())
print(filme.keys())
print(filme.items())

for k,v in filme.items():
    print(f'O {k} é {v}.')

for k in filme.values():
    print(k)
for k in filme.keys():
    print(k)
for k in filme.items():
    print(k)

locadora=filme,dados
print(locadora)
print(locadora[0]['ano'])

pessoas={'nome':'Juan','sexo':'M','idade': 25}
print(pessoas['nome'])
#print(pessoas[0]) nao funciona. precisa declarar oq vc busca
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos.')
for k,v in pessoas.items():
    print(f'{k} = {v}')

pessoas['nome']='Fábio' #mudando nome
print(pessoas)
pessoas['peso']=70 #adiciona um novo elemento
print(pessoas)

brasil=[]
estado1={'uf':'Rio de Janeiro','sigla':'RJ'}
estado2={'uf':'São Paulo','sigla':'SP'}
brasil.append(estado1)
brasil.append(estado2)
print(brasil)
print(brasil[0]['uf'])
print(brasil[1]['sigla'])

estado=dict()
brasil=list()
for c in range (0,3):
    estado['uf']=str(input('Unidade Federativa: '))
    estado['sigla']=str(input('Sigla do Estado: '))
    brasil.append(estado.copy()) #apenas usar estado[:] nao funciona em um dicionario
print(brasil)

for est in brasil:
    """for k,v in est.items():
        print(f'O campo {k} tem valor {v}.')"""
    for v in est.values():
        print(v)
