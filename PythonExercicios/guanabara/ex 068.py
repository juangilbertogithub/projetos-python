import random
from time import sleep

cont=0
escolhacomputador=''

while True:
    cont+=1
    valorcomputador=random.randint(1,10)
    valor=int(input('\033[1;97mDigite um valor (1 a 10): '))
    escolha=str(input('Par ou Ímpar?: ')).upper().strip()[0]

    totalvalor = valor + valorcomputador
    resultado= totalvalor%2

    print('')
    print('Calculando', end='')
    for ponto in range(1,4):
        print('.', end = '')
        sleep(0.75)
    print('\n')

    if resultado == 0 and escolha == 'P':
        print('\033[1;32mVocê venceu! O resultado foi PAR.\033[m')
        print(f'\033[1;97mVocê jogou {valor} e o computador jogou {valorcomputador}.')
        print('')
    elif resultado == 0 and escolha == 'I':
        print('\033[1;31mVocê perdeu! O resultado foi PAR.\033[m')
        print(f'\033[1;97mVocê jogou {valor} e o computador jogou {valorcomputador}.')
        cont-=1
        break

    elif resultado == 1 and escolha == 'I':
        print('\033[1;32mVocê venceu! O resultado foi ÍMPAR.\033[m')
        print(f'\033[1;97mVocê jogou {valor} e o computador jogou {valorcomputador}.')
        print('')
    elif resultado == 1 and escolha == 'P':
        print('\033[1;31mVocê perdeu! O resultado foi ÍMPAR.\033[m')
        print(f'\033[1;97mVocê jogou {valor} e o computador jogou {valorcomputador}.')
        cont-=1
        break

sleep (1)
print('')

if cont == 0:
    print(f'\033[1;97mVocê não ganhou nenhuma vez seguida.')
elif cont == 1:
    print('\033[1;97mVocê ganhou apenas uma vez.')
else:
    print(f'\033[1;97mVocê ganhou {cont} vezes seguidas antes de perder.')

"""if escolha != 'P':
    escolhacomputador = 'I'
if escolha == 'I':
    escolhacomputador = 'P'
print('Essa opção não existe. Por favor, tente novamente)"""