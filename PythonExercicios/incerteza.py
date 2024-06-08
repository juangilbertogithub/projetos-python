from math import sqrt
lista=[]
ok=True
while ok==True:
    valores=float(input(f'Insira o valor {len(lista)+1} ("12345" para parar): '))
    lista.append(valores)
    if valores==12345:
        lista.pop()
        break

media=sum(lista)/len(lista)
print(f'A média foi de {media:.3f}')


calculo_incerteza_de_cada_uma=0
for c in lista:
    print(c)
    calculo_incerteza_de_cada_uma = calculo_incerteza_de_cada_uma =+ (c-media)**2
    print(calculo_incerteza_de_cada_uma)
incerteza_de_cada_uma=(calculo_incerteza_de_cada_uma/len(lista)-1)**(1/2)
print(f'A incerteza de cada uma é {incerteza_de_cada_uma:.3f}')

incerteza_da_media=incerteza_de_cada_uma/(len(lista))**(1/2)
print(f'A incerteza da média é de {incerteza_da_media:.3f}')

