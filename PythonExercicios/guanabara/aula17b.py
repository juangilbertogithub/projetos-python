"""num=[2,5,9,1]
num[2]=3
num.append(7) #adiciona no final
num.sort() #organiza
num.sort(reverse=True) #organiza invertido
num.insert(2,0) #inserte o valor 0 na posiçao 2
num.pop(1) #remove o elemento desse ponto
num.pop() #remove o ultimo elemento da lista
num.remove(8) #remove o primeiro valor 8 da lista
num.remove('9') #remove especificamente oq tem esse nome na lista
#quando algo é removido, ele indexa novamente a quantidade da lista sem oq foi removido
if 8 in num: #remove o 8 se estiver na lista
    num.remove(8)
else:
    print('Não encontrei o número 8 pra remover )=')
print(num)
print(f'Essa lista tem {len(num)} elementos.')"""


"""valores=[] #ou valores=list() ou valores=list(range(4,11))
valores.append(5)
valores.append(9)
valores.append(4)

for v in valores:
    print(f'{v}', end= ' ')

for c,v in enumerate (valores):
    print(f'O valor {v} está na posição {c}')"""

"""valores=[]
for cont in range (0,5):
    valores.append(int(input('Insira um valor: '))) #ler valores pelo teclado e por na lista
for c,v in enumerate (valores): #aplicando os valores aplicados em algo qualquer
    print(f'O valor {v} está na posição {c}')"""

"""a=[2,3,4,7]
b=a #o python cria uma ligação entre as listas
b[2]=8 #entao se eu faço isso, eu mudo as duas listas ao mesmo tempo. vc n esta fazendo uma copia dessa forma
print(f'Lista A: {a}')
print(f'Lista B: {b}')"""

"""a=[2,3,4,7]
b=a [:] #o python cria uma ligação entre as listas. nesse caso, uma copiaeu crio uma copia
b[2]=8 
print(f'Lista A: {a}')
print(f'Lista B: {b}')"""