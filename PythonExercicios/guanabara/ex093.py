dicionario={}
gols=[]
print('-'*30)
dicionario['jogador']=str(input('Digite o nome do jogador: ')).capitalize().strip()
numero=int(input('Quantidade de partidas: '))
for c in range (0, numero):
    gols.append(int(input(f'Gols na partida {c+1}: ')))
dicionario['gols']=gols
dicionario['golstotais']=sum(gols)

print('-'*30)
print(dicionario)
print('-'*30)
for k,v in dicionario.items():
    print(f'O campo {k} tem o valor {v}.')
print('-'*30)
print(f'O jogador {dicionario["jogador"]} jogou {numero} partidas.')
for i, v in enumerate(dicionario['gols']):
    print(f'Na partida {i+1} fez {v} gols.')
print('-'*30)