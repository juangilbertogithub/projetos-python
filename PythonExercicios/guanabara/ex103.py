"""def ficha(nome='',gols=''):
    if nome=='':
        nome='<desconhecido>'
    if gols=='':
        gols=0
    print(f'O jogador {nome} fez {gols} gols.')

nome=str(input('Digite o nome do jogador: ')).strip().capitalize()
gols=str(input('Insira o número de gols: '))
ficha(nome,gols)"""

def ficha(nome='<desconhecido>',gols=0):
    print(f'O jogador {nome} fez {gols} gols.')

nome=str(input('Digite o nome do jogador: ')).strip().capitalize()
gols=str(input('Insira o número de gols: '))
if gols.isnumeric():
    gols=int(gols)
else:
    gols=0
ficha(nome,gols)