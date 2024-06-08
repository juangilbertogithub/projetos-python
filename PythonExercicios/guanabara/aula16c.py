lanche='hamburguer' #preenche um espaço reservado na memoria
lanche='suco' #o suco substitui. é uma variavel simples

lanche=('hamburguer', 'suco', 'pizza', 'pudim') #variavel composta com cada um sendo responsavel por um valor
print(lanche[2])#ele mostra a pizza
print(lanche[0:2])#mostra o hamburguer e o suco
print(lanche[1:])
print(lanche[-1])

len(lanche) #quantas coisas na lista

for comida in lanche: #mostra aquele item. funciona alem do in range
    print(comida)

for c in range (0,len(lanche)):
    print(c) #posiçao
    print(lanche[c]) #item na posiçao da lista

for pos, comida in enumerate (lanche): #da o dado e a posiçao
    print(f'A comida {comida} está na posição {pos}.')


print(sorted(lanche)) #ordena sem mudar

a=(2,5,4)
b=(5,8,1,2)
c=a+b #que é diferente de c=b+a
print(c)
print(len(c)) #vai mostrar quanto tem no total
print(c.count(5)) #conta quantas vezes aparece o 5 na tupla c
print(c.index(8)) #mostra em q posiçao está o numero 8
print(c.index(5,1)) #mostra em q posiçao está o numero 5. o 1 indica daonde irá começar a contagem

pessoa='Juan', 25, 'M', 52 #posso misturar numero e palavras
print(pessoa)

del(pessoa) #n posso modificar, mas posso apagar uma tupla inteira