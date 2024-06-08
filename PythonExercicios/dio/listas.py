frutas=['uva', 'maça','laranja']
print(frutas[0]) #uva
print(frutas[-1]) #laranja

frutas=[] #lista vazia
print(frutas)

letras=list('python') #cada letra é um elemento
print(letras)

numeros=list(range(10)) #cada letra é um elemento usando um range colocando um valor pra cada espaço
print(numeros)

carro=['Ferrari','F8',2020, 42.0003200,'São Paulo', True] #varias coisas diferentes

matriz=[
    [1, "a", 2],
    ["b", 3, 4],
    [6, 5, "c"]
]

print(matriz[0]) #[1,'a',2]
print(matriz[0][0]) #1
print(matriz[0][-1]) #2
print(matriz[-1][-1]) #c

lista=['p','y','t','h','o','n']

print(lista[2:])
print(lista[:2])
print(lista[1:3])
print(lista[0:3:2])
print(lista[::])
print(lista[::-1])

carros=['gol','celta','palio']
for carro in carros:
    print(carro)


carros=['gol','celta','palio']
for indice,carro in enumerate(carros):
    print(f'Na posição {indice+1} está o carro: {carro.title()}.')

#filtro versao 1
numeros=[1,30,21,2,9,65,34]
pares=[]
for numero in numeros:
    if numero%2==0:
        pares.append(numero)
        print(f'Número {numero} adicionado a lista dos pares.')
print(pares)

#filtro versao 2
numeros=[1,30,21,2,9,65,34]
pares=[numero for numero in numeros if numero%2==0]

#filtro modificado versao 1
numeros=[1,30,21,2,9,65,34]
quadrado=[]
for numero in numeros:
    quadrado.append(numero**2)

#filtro modificado versao 2
numeros=[1,30,21,2,9,65,34]
quadrado=[numero**2 for numero in numeros]


lista=[]
lista.append(1) #adicionando item a lista
lista.append('Python')
lista.append([40,30,20])
print(lista)

lista1=[1,'Python',[40,30,20]]
lista2=lista1.copy()
lista2[0]=2
print(lista1)
print(lista2)

cores=['vermelho','azul','verde','azul']
print(cores.count('vermelho'))
print(cores.count('azul'))
print(cores.count('verde'))

linguagem=['portugues','ingles']
print(linguagem)
linguagem.extend(['japones','espanhol'])
print(linguagem)

print(linguagem.index('ingles'))
print(linguagem.index('espanhol'))

linguagem=['portugues','ingles', 'espanhol', 'japones']
linguagem.pop() #tira o japones
linguagem.pop(0) #tira o portugues
print(linguagem)

linguagem=['portugues','ingles', 'espanhol', 'japones']
linguagem.remove('ingles') #tira palavras especificas
print(linguagem)

linguagem=['portugues','ingles', 'espanhol', 'japones']
linguagem.reverse() #inverte
print(linguagem)

linguagem=['portugues','ingles', 'espanhol', 'japones']
linguagem.sort()
print(linguagem)
linguagem.sort(reverse=True)
print(linguagem)

linguagem=['portugues','ingles', 'espanhol', 'japones']
print(len(linguagem))

linguagem=['portugues','ingles', 'espanhol', 'japones']
print(sorted(linguagem, key=lambda x:len(x)))
print(sorted(linguagem))

linguagem=['portugues','ingles', 'espanhol', 'japones']
print(sorted(linguagem, key=lambda x:len(x), reverse=True))

frutas=('laranja','pera','uva',)
print(frutas)
letras=tuple('python')
print(letras)
numeros=tuple([1,2,3,4])
print(numeros)
pais=('Brasil',)
print(pais)

print(frutas[0])
print(frutas[-1])

matriz=(
    (1,'a',2),
    ('b',3,4),
    (5,6,'c'),
)
print(matriz[0])
print(matriz[0][0])
print(matriz[0][-1])
print(matriz[-1][-1])


carros = ("gol")
print(isinstance(carros, tuple))


numeros=set([1,2,3,1,3,4])
print(numeros)

fruta=set('abacaxi')
print(fruta)

carros=set(('palio','gol','celta','palio'))
print(carros)

numeros={1,2,3,4}
numeros=list(numeros)
print(numeros[0])

carros={'gol','celta','palio'}
for carro in carros:
    print(carro)

carros={'gol','celta','palio'}
for indice, carro in enumerate(carros):
    print(f' {indice+1}:{carro}')

conjunto_a={1,2}
conjunto_b={3,4}
conjunto_ab=conjunto_a.union(conjunto_b)
print(conjunto_ab)

conjunto_a={1,2,3}
conjunto_b={2,3,4}
conjunto_ab=conjunto_a.intersection(conjunto_b)
print(conjunto_ab)

conjunto_a={1,2,3}
conjunto_b={2,3,4}
conjunto_ab=conjunto_a.difference(conjunto_b)
print(conjunto_ab)
conjunto_ab=conjunto_b.difference(conjunto_a)
print(conjunto_ab)

conjunto_a={1,2,3}
conjunto_b={2,3,4}
conjunto_ab=conjunto_a.symmetric_difference(conjunto_b)
print(conjunto_ab)

conjunto_a={1,2,3}
conjunto_b={4,1,2,5,6,3}
conjunto_ab=conjunto_a.issubset(conjunto_b)
print(conjunto_ab)
conjunto_ab=conjunto_b.issubset(conjunto_a)
print(conjunto_ab)

conjunto_a={1,2,3}
conjunto_b={4,1,2,5,6,3}
conjunto_ab=conjunto_a.issuperset(conjunto_b)
print(conjunto_ab)
conjunto_ab=conjunto_b.issuperset(conjunto_a)
print(conjunto_ab)

conjunto_a={1,2,3,4,5}
conjunto_b={6,7,8,9}
conjunto_c={0,1}
print(conjunto_a.isdisjoint(conjunto_b))
print(conjunto_a.isdisjoint(conjunto_c))

sorteio={1,23}
sorteio.add(25)
sorteio.add(42)
sorteio.add(25)
print(sorteio)

sorteio={1,23}
sorteio.clear()
print(sorteio)

sorteio={1,23}
sorteio.copy()
print(sorteio)

numeros={1,2,3,1,2,4,5,5,6,7,8,9,0}
print(numeros)
numeros.discard(1)
numeros.discard(45)
print(numeros)

numeros={1,2,3,1,2,4,5,5,6,7,8,9,0}
print(numeros)
numeros.pop()
numeros.pop()
print(numeros)

numeros={1,2,3,1,2,4,5,5,6,7,8,9,0}
print(numeros)
numeros.remove(1)
#numeros.remove(45) da erro por n existir. o fato de dar erro pode ser util em algumas ocasioes
print(numeros)

numeros={1,2,3,1,2,4,5,5,6,7,8,9,0}
print(1 in numeros)
print(10 in numeros)