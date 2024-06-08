from random import randint
print("""JOKENPÔ
Escolha uma das opções:
1 - PARA PEDRA
2 - PARA PAPEL
3 - PARA TESOURA""")
jogador=int(input('Sua opção: '))
while jogador != 1 and jogador != 2 and jogador != 3:
    print("""Opção inválida!
1 - PARA PEDRA
2 - PARA PAPEL
3 - PARA TESOURA""")
    jogador = int(input('Sua opção: '))
computador=randint(1,3)
print(f'Você escolheu {jogador} e o computador escolheu {computador}.')
if jogador == computador:
    print('Empate!')
elif jogador == 1 and computador == 3 or jogador == 2 and computador == 1 or jogador == 3 and computador == 2:
    print('Você venceu!')
else:
    print('Você perdeu!')

#Sabendo como funciona o jogo crie uma variável para cada jogador que deve
#armazenar a opção escolhida pela criança (Pedra, Papel ou Tesoura) e apresente o
#resultado da jogada.