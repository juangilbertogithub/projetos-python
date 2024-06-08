"""from random import randint
contagem=0

while True:

    escolhajogador=str(input('Escolha Par ou Ímpar: ')).strip().capitalize()
    escolhacomputador=''
    if escolhajogador=='Par':
        escolhacomputador='Ímpar'
    elif escolhajogador=='Ímpar' or escolhajogador=='Impar':
        escolhacomputador='Par'

    computador=randint(0,10)
    jogador=int(input('Digite um valor entre 0 e 10: '))
    valor = computador+jogador
    if valor%2==0 and escolhajogador=='Par':
        print('Jogador vence!')
        contagem+=1
        print(f'Você inseriu {escolhajogador}, o computador inseriu {escolhacomputador} e o valor foi {valor}.')
    elif valor%3==0 and escolhajogador=='Ímpar':
        print('Jogador vence!')
        contagem += 1
        print(f'Você inseriu {escolhajogador}, o computador inseriu {escolhacomputador} e o valor foi {valor}.')

    elif valor%2!=0 and escolhajogador=='Ímpar':
        break
        print('Jogador perdeu!')
        print(f'Você inseriu {escolhajogador}, o computador inseriu {computador} e o valor foi {valor}.')

    elif valor%3!=0 and escolhajogador=='Ímpar':
        break
        print('Jogador perdeu!')
        print(f'Você inseriu {escolhajogador}, o computador inseriu {escolhacomputador} e o valor foi {valor}.')

print(f'Você perdeu. O computador escolheu {escolhacomputador} e o valor foi {valor}. Você ganhou {contagem} vezes consecutivas.')"""

from random import randint
cont=0

while True:

    parouimpar = ' '
    while parouimpar not in 'PI':
        parouimpar = str(input('Par ou Impar? ')).strip().upper()[0]

    numero=int(input('Digite um número de 0 a 10: '))
    computador=randint(0,10)
    valor=computador+numero

    if valor%2==0:
        if parouimpar=='P':
            cont+=1
            print('Você venceu.')
        else:
            break

    elif valor % 2 != 0:
        if parouimpar=='I':
            cont += 1
            print('Você venceu.')
        else:
            break

if parouimpar=='P':
    print(f'Você perdeu após {cont} vitórias. O valor deu {valor} e você escolheu Par.')
if parouimpar=='I':
    print(f'Você perdeu após {cont} vitórias. O valor deu {valor} e você escolheu Ímpar.')