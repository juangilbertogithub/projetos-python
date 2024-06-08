"""import random
from time import sleep

print('\033[1;97mJokenpô\n')

sleep (1)

n=str(input('Digite Pedra, Papel ou Tesoura: ')).strip().capitalize()
lista=['Pedra', 'Papel', 'Tesoura'] #pedra, papel, tesoura

resultado=random.choice(lista)

print('\nCalculando resultado...\n')

sleep(3)

if resultado=='Tesoura':
    if n=='Pedra':
        print(f'\033[1;32mVocê venceu! Você escolheu {n} e a máquina escolheu {resultado}.')
    if n=='Papel':
        print(f'\033[1;31mVocê perdeu! Você escolheu {n} e a máquina escolheu {resultado}.')
    if n==resultado:
        print(f'\033[1;33mEMPATE! Os dois escolheram {n}')

if resultado=='Papel':
    if n=='Tesoura':
        print(f'\033[1;32mVocê venceu! Você escolheu {n} e a máquina escolheu {resultado}.')
    if n=='Pedra':
        print(f'\033[1;31mVocê perdeu! Você escolheu {n} e a máquina escolheu {resultado}.')
    if n==resultado:
        print(f'\033[1;33mEMPATE! Os dois escolheram {n}')

if resultado=='Pedra':
    if n=='Papel':
        print(f'\033[1;32mVocê venceu! Você escolheu {n} e a máquina escolheu {resultado}.')
    if n=='Tesoura':
        print(f'\033[1;31mVocê perdeu! Você escolheu {n} e a máquina escolheu {resultado}.')
    if n==resultado:
        print(f'\033[1;33mEMPATE! Os dois escolheram {n}')"""

from random import randint

itens= ('Pedra', 'Papel', 'Tesoura')
computador=randint(0,2)

print("""0- Pedra
1- Papel
2- Tesoura""")
jogador=int(input('Escolha uma opção: '))

print(f'O computador jogou {itens[computador]}')
print(f'O jogador jogou {itens[jogador]}')

if computador==0: #computador pedra
    if jogador==0:
        print('EMPATE')
    elif jogador==1:
        print('JOGADOR VENCEU')
    elif jogador==2:
        print('COMPUTADOR VENCEU')
elif computador==1: #computador papel
    if jogador==0:
        print('COMPUTADOR VENCEU')
    elif jogador==1:
        print('EMPATE')
    elif jogador==2:
        print('JOGADOR VENCEU')
elif computador==2: #computador tesoura
    if jogador==0:
        print('COMPUTADOR VENCEU')
    elif jogador==1:
        print('JOGADOR VENCEU')
    elif jogador==2:
        print('EMPATE')