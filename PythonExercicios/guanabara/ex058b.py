from random import randint
from time import sleep
computador=randint(0,10)
tentativas=0

print('Hm... deixa eu pensa em um número entre 0 e 10.')
sleep(3)
print('Pronto! Vamos ver se você consegue acertar.')
sleep(1)

jogador=int(input('Insira um valor: '))
while jogador != computador:
    tentativas+=1
    print('Você errou! Tente novamente.')

    if jogador < computador:
        print('Mais...')
    elif jogador > computador:
        print('Menos...')

    jogador=int(input('Insira um valor: '))

"""print('Você venceu! Você acertou de primeira!') if tentativas==0 else print(f'Você acertou na {tentativas+1}ª tentativa!')"""

if tentativas==0:
    print(f'Você venceu! Você acertou de primeira!')
else:
    print(f'Você acertou na {tentativas+1}ª tentativa!')