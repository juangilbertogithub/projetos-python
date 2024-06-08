lista=[]
resposta='S'

num=lista.append(int(input('Insira um valor: ')))
while True:
    num=(int(input('Insira um valor: ')))
    if num not in lista:
        lista.append(num)
    elif num in lista: #ou simplesmente por else
        print('Esse valor já foi adicionado anteriormente')

    resposta=str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    if resposta=='N':
        break

lista.sort()
print(f'Lista em ordem crescente: {lista}')