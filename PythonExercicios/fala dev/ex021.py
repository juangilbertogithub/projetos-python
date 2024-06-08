from random import randint
valor_jogador=int(input('Digite um valor entre 2 e 12: '))
if valor_jogador < 2 or valor_jogador > 12:
    print('Valor inválido')
else:
    dado_computador_1=randint(1,6)
    dado_computador_2=randint(1,6)
    soma=dado_computador_1+dado_computador_2
    print(f'Você escolheu {valor_jogador}. A soma deu {soma}')
    if soma==valor_jogador:
        print('Você venceu!')
    else:
        print('Você perdeu!')

#Esse é o jogo dos dados, muito usado em Las Vegas nos cassinos, aposte em um número que seja o resultado da soma deles e
#ganhe o seu dinheiro. Crie duas variáveis para representar os dados e uma para sua aposta, crie uma para armazenar o resultado e faça a verificação.