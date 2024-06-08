lista=[]
num=int(input('Digite um valor: '))
lista.append(num)
for c in range (1,5):
    num=(int(input('Digite um valor: ')))
    if num >= max(lista):
        lista.append(num)
        print('Valor inserido na posição final.')
    elif num <= min(lista):
        lista.insert(0,num)
        print('Valor inserido no início.')
    elif min(lista) < num < max(lista):
        lista.insert(3,num)
        print('Valor inserido na posição do meio.')

print(f'A lista completa fica {lista}.')


"""elif min(lista) > num < max(lista):
    lista.append()
    print('Valor inserido no meio')"""