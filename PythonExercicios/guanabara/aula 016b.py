lanche=('Hamburguer', 'Suco', 'Pizza', 'Pudim')
print(lanche[1])
print(lanche[-2])
print(lanche[1:3])
print(lanche[2:])
print(lanche[:2])
print(lanche)

#lanche[1]= 'Refrigerante' não funciona por listas serem imutáveis

for comida in lanche: #maneira 1
    print(comida)

len(lanche)

for cont in range (0, len(lanche)):  #maneira 2
    print(cont)
    print(lanche[cont])

for pos,comida in enumerate (lanche): #enumerate da o dado e o numero da minha lista  #maneira 3
    print (f'posição {pos}, comida {comida}')

print(sorted(lanche)) #nao altera, apenas poem em ordem alfabetica

a=('c', 'a', 'b')
b=('e', 'f', 'd')
c= a+b
print(c)
print(len(c))
print (sorted(c))
print(c.count('b')) #quantas vezes aparece o ''b'' dentro de c
print(c.index('f')) #mostra em que posiçao esta o ''f''
print(c.index('f', 5)) #mostra em que posiçao esta o ''f'' a partir da posição 5

pessoa= ('Juan', 23, 'M', 49.9) #posso misturar tipos diferentes em uma tupla
print(pessoa)
del(pessoa) #posso deletar a minha tupla inteira. n tem como apagar apenas um elemento dela