nome=str(input('Insira seu nome: ')).strip()
nomedividido=nome.split()
nomeinvertido=nomedividido[::-1]

print(f'Seu primeiro nome é {nomedividido[0]} e seu último nome é {nomeinvertido[0]}.') #ou nomedividido[len(nomedividido)-1]