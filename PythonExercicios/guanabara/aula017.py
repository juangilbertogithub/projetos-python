#listas são mutáveis
lanche=['hamburguer','refrigerante','pizza','pudim']

lanche[3]='picole' #ele destroi o anterior e substitui
lanche.append('biscoito') #ele substitui o último
lanche.insert(0,'hotdog') #insere no lugar do primeiro e empurra o resto uma casa pro lado (ainda mantendo o primeiro que substituiu)

del lanche[3]#remove o que está nesse valor
lanche.pop() #remove o ultimo, seu índice e chave
lanche.pop(3) #remove daquela posiçao
lanche.remove('pizza') #remove aquela palavra especifica
if 'pizza' in lanche: #se não tiver certeza se o elemento já foi removido e pra não dar erro
    lanche.remove('pizza')

valores=list(range(4,11)) #poderia fazer pulando de 2 em 2, por exemplo. range(4,11,2)
len(valores)

valores=[8,2,5,4,9,3,0]
len(valores)

valores=[8,2,5,4,9,3,0]
valores.sort()
len(valores)

valores=[8,2,5,4,9,3,0]
valores.sort(reserve=True)
len(valores)

num=[2,5,9,1]
num.insert(2,0)
num.pop(2)
num.pop(3) #checar a diferença


#terao muitos exercicios onde ele vai ler valores, colocar dentro de listas, analisar e colocar pra frente
valores=[] #ou valores=list()
valores.append(5)
valores.append(9)
valores.append(4)

for v in valores:
    print(f'{v}', end=' ')

for c,v in enumerate(valores):
    print(f'Na posição {c} está o valor {v}.')

for cont in range (0,5):
    valores.append(int(input('Digite um valor: ')))

#PARTE 2

dados=[]
dados.append('Pedro')
dados.append(25)
print(dados[0])
print(dados[1])

pessoas=[]
pessoas.append(dados[:]) #ou pessoas=[['Pedro', 25],['Maria',19],['Joao',32]]
print(pessoas[0,0])
print(pessoas[1,1])
print(pessoas[2,1])
print(pessoas[1])

teste=[]
teste.append('Gustavo')
teste.append(40)
galera=[]
galera.append(teste)
print(galera)

teste=[]
teste.append('Gustavo')
teste.append(40)
galera=[]
galera.append(teste)
teste[0]='Maria'
teste[1]=22
print(galera)
#os dois ficam com 'Maria',22 porque eu liguei as duas. se mudei o teste, mudou a galera

teste=[]
teste.append('Gustavo')
teste.append(40)
galera=[]
galera.append(teste[:]) #o certo que ele copia
teste[0]='Maria'
teste[1]=22
print(galera)

galera=[['João',19]['Ana',33]['Joaquim',13]['Maria',45]]
print(galera[0])
print(galera[0][0])
print(galera[2][1])
for p in galera:
    print(p[0])
    print(f'{p[0]} tem {p[1]} anos.')

galera=[]
dado=[]
for c in range (0,3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:]) #copia dos dados
    dado.clear()
print(galera)

for c in galera
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade')
    else:
        print(f'{p[0]} é menor de idade')

galera=[]
dado=[]
for c in range (0,3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado) #gera listas vazias
    dado.clear()
print(galera)

