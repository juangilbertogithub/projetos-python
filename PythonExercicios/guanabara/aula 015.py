"""cont=1
while cont<=10:
    print(cont, end=' ')
    cont+=1
print ('Acabou')"""

"""cont=1
while True:
    print(cont, end=' ')
    cont+=1
    if cont==10:
        break
print ('Acabou')"""

n=0
s=0
while n!=999:
    n=int(input('Digite um número: '))
    if n==999:
        break
    s+=n

print (f'A soma vale {soma}.')