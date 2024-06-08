from random import randint
from time import sleep
n=int(input('Digite um número entre 0 e 5: '))
sorte=randint(0,5)
if n==sorte:
    print('Parabéns, você acertou!')
else:
    print('Processando...')
    sleep(1)
    print(f'Você errou! Eu pensei em {sorte}, não {n}.')