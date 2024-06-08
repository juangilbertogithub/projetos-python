from time import sleep

jogadores=[]
dicionario={}
gols=[]
print('-'*30)
while True:
    dicionario['Jogador']=str(input('Digite o nome do jogador: ')).capitalize().strip()
    numero=int(input('Quantidade de partidas: '))
    for c in range (0, numero):
        gols.append(int(input(f'Gols na partida {c+1}: ')))
    dicionario['Gols']=gols[:]
    dicionario['Gols totais']=sum(gols)
    jogadores.append(dicionario.copy())
    print(jogadores)
    resp=str(input('Deseja continuar? Sim ou Não: '))[0].strip().upper()
    if resp=='N':
        break

"""print('cod ', end='')
for i in dicionario.keys():
    print(f'{i:<15}',end='')
print()
for k,v in enumerate(jogadores):
    print(f'{k:>4} ',end='')
    for c in v.values():
        print(f'{str(c):<15}',end='')
    print()

while True:
    escolha=int(input('Mostrar os dados de qual jogador? (999 para parar)'))
    print(escolha-1)
    if escolha == 999:
        break
    if escolha >= len(jogadores):
        print('Erro! Esse código não existe.')
    else:
        print(f'Levantamento do jogador {jogadores[escolha]["nome"]}')"""


print('-' * 30)
print('Código, Nome, Gols e Gols totais, respectivamente:')
print('-' * 30)
cont=1
for c in jogadores:
    print(cont, end= ' ')
    cont+=1
    for k,v in c.items():
        print(k, v, end= ' ')
    print()

print('-' * 30)
while True:
    escolha=int(input('Mostrar os dados de qual jogador? (999 para parar)'))
    if escolha == 999:
        break
    if escolha >= len(jogadores):
        print('Erro! Esse código não existe.')
    else:
        """for k,v in jogadores[escolha].items():"""
        print(jogadores[escolha-1]["Gols"])
    print('-' * 30)

print(jogadores)
print('FIM')

#sei la, tem algo estranho nesse codigo q n entendo pq n funciona