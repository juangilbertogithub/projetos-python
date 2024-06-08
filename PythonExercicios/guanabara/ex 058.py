from random import randint

"""tentativa=0
computador=randint(1,10)

jogador=int(input('Pensei em um número entre 1 e 10. Consegue adivinhar qual? Digite um número: '))

while jogador != computador:
    tentativa+=1
    if jogador>computador:
        print('Menos. Tente novamente.')
    if jogador<computador:
        print('Mais. Tente novamente.')

    jogador=int(input('Digite outro valor: '))

print(f'Você acertou com {tentativa} tentativas! O número era o {computador}.')"""


computador =randint(1,10)
print('Pensei em um número entre 1 e 10.')
jogador=int(input('Digite um palpite: '))
acertou= False #ensinou a usar true e false no while
palpite=0
while not acertou:
    palpite+=1
    if computador ==jogador:
        acertou=True

    else:
        if computador > jogador:
            print('Mais. Tente novamente')
            jogador=int(input('Digite um novo palpite: '))
        if computador < jogador:
            print('Menos. Tente novamente')
            jogador = int(input('Digite um novo palpite: '))

print(f'Acertou! Você precisou de {palpite} tentativas')