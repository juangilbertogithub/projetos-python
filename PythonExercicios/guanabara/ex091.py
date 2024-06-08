from random import randint
from time import sleep
from operator import itemgetter

print('-='*20)
print('Valores sorteados')
print('-='*20)

jogadores= {'jogador 1':randint(1,6),
            'jogador 2':randint(1,6),
            'jogador 3':randint(1,6),
            'jogador 4':randint(1,6)}

for k,v in jogadores.items():
    print(f'O {k.capitalize()} tirou {v}.')
    sleep(0.5)

print('-='*20)
ranking= sorted(jogadores.items(), key=itemgetter(1),reverse=True)

for i,v in enumerate(ranking):
    print(f'{i+1}º lugar: O {v[0].capitalize()} tirou {v[1]}.')
    sleep(0.5)

print('-='*20)
print('FIM DO JOGO')