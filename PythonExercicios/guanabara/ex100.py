from random import randint
lista = []


def sorteio(): #posso fazer com ou sem a palavra lista dentro das funçoes e pedido pra mostrar a funçao
    print(f'Os 5 valores sorteados da lista foram: ', end='')
    for c in range (5):
        numero=randint(1,9) #posso fazer direto, mas fiz assim so pra mostrar os numeros adicionados
        lista.append(numero)
        print(f'{numero}', end=' ')
    print()


sorteio()


def somaPar():
    soma = 0
    for c in lista:
        if c%2==0:
            soma+=c
    print(f'A soma dos valores pares é {soma}.')


somaPar()
