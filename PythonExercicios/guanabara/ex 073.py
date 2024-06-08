
lista=('Corinthians', 'América-MG', 'Bragantino', 'Atlético-MG','Coritiba','São Paulo','Santos', 'Cuiabá','Internacional', 'Avaí','Palmeiras', 'Flamengo', 'Botafogo','Fluminense','Ceará','Athletico-PR','Atlético-GO','Goiás','Juventude','Fortaleza')

print(lista[0:6])
print(lista[16:]) #ou print(lista[-4:])
print(sorted(lista))
print(f'Coritiba está na posição {lista.index("Coritiba") + 1}.')
