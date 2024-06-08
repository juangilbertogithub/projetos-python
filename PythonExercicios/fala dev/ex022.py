from random import randint
escolha_computador=0
escolha_jogador=str(input('Escolha Par ou Ímpar: ')).strip().upper()[0]
if escolha_jogador == 'P':
    escolha_computador = 'I'
    print('Você escolheu Par, logo, o computador escolheu Ímpar.')
elif escolha_jogador == 'I':
    escolha_computador = 'P'
    print('Você escolheu Ímpar, logo, o computador escolheu Par.')
jogador=int(input('Insira um valor entre 0 e 10: '))
print(f'Você escolheu o valor {jogador}.')
maquina=randint(0,10)
print(f'A máquina escolheu o valor {maquina}.')
soma=jogador+maquina
print(f'A soma deu {soma}. Ou seja,',end=' ')
if soma%2==0:
    print('par!')
    if escolha_jogador=='P':
        print('O jogador venceu!')
    elif escolha_jogador=='I':
        print('O computador venceu!')
elif soma%2==1:
    print('ímpar!')
    if escolha_jogador=='I':
        print('O jogador venceu!')
    elif escolha_jogador=='P':
        print('O computador venceu!')

#O Jogo do par ou ímpar é usado onde duas pessoas jogam geralmente para decidir um impasse, cada um escolhe entre par ou
#ímpar e mostra o seu número, a soma entre eles resulta em um número par ou ímpar e assim é decidido o vencedor. Aqui
#faremos com a máquina, ela escolherá um número randômico entre 0 e 10 e você escolherá o seu.