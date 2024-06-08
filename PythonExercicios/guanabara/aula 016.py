""""# lanche[1]='Refrigerante' tuplas são imutaveis

lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim')
print(lanche[1])
print(lanche[1:3])
print(lanche[2])
print(lanche[:2])
print(lanche[-2])
print(lanche[-3])
print(lanche)

print(len(lanche))

print(sorted(lanche))

for comida in lanche: #nao mostra a posiçao
    print(f'Vou comer {comida}')

for cont in range (0,len(lanche)): #pode mostrar a posiçao
    print (cont)
    print(lanche[cont])

for pos, comida in enumerate(lanche):
    print(f'Comida {comida} na posição {pos}')"""


"""a = (2,5,4)
b=(5,8,1,2)
c=a+b
print(c) #junta as duas tuplas
print(len(c))
print(c.count(5)) #quantas vezes aparece o número 5 nas tuplas
print(c.index(8)) #mostra em que posiçao está o 8 """

pessoa=('Juan', 23, 'M', 50.1) #posso misturar tipos diferentes de dados nas tuplas
print(pessoa)
del(pessoa) #nao posso mexer a minha tupla, mas posso deletar ela
