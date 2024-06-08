resp='S'
lista=[]

while resp=='S':
    num=int(input('Digite um valor: '))
    if num not in lista:
        lista.append(num)
        print('Valor adicionado.')
    else:
        print('Esse valor já foi adicionado a lista anteriormente.')

    resp=str(input('Deseja continuar? [Sim/Não]: ')).strip().upper()[0]

lista.sort()
print(f'Os números da sua lista são {lista}')
#ou print(sorted(lista))