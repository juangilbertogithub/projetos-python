from time import sleep
from random import randint

print('JO')
sleep(0.4)
print('KEN')
sleep(0.4)
print('PÔ')
sleep(0.4)

print()
computador=randint(1,3)

print('''Vamos jogar! Escolha um valor:
1- Pedra
2- Papel
3- Tesoura''')

print()
jogador=int(input())

print()

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ')
sleep(1)

print()

if computador == jogador:
    print('EMPATAMOS')
    if jogador == 1:
        print('Nós dois escolhemos pedra.')
    elif jogador == 2:
        print('Nós dois escolhemos papel.')
    elif jogador == 3:
        print('Nós dois escolhemos Tesoura.')

elif computador == 1 and jogador == 2:
    print('Você venceu!')
    print('Eu escolhi Pedra e você escolheu Papel.')

elif computador == 1 and jogador == 3:
    print('Você perdeu.')
    print('Eu escolhi Pedra e você escolheu Papel.')

elif computador == 2 and jogador == 1:
    print('Você perdeu.')
    print('Eu escolhi Papel e você escolheu Pedra.')
elif computador == 2 and jogador == 3:
    print('Você venceu!')
    print('Eu escolhi Papel e você escolheu Tesoura.')

elif computador == 3 and jogador == 1:
    print('Você venceu!')
    print('Eu escolhi Tesoura e você escolheu Pedra.')

elif computador == 3 and jogador == 2:
    print('Você perdeu.')
    print('Eu escolhi Tesoura e você escolheu Papel')

"""itens=('Pedra','Papel','Tesoura')
computador=randint(0,2)
print(itens[computador])"""