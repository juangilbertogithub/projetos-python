import moeda

p=float(input('Digite o preço: R$'))

print(f'O valor aumentado em 10% de {moeda.moeda(p)} é {moeda.moeda(moeda.aumentar(p, 10))}')
print(f'O valor diminuido em 13% de {moeda.moeda(p)} é {moeda.moeda(moeda.diminuir(p, 13))}')
print(f'O dobro de {moeda.moeda(p)} é {moeda.moeda(moeda.dobro(p))}')
print(f'A metade de {moeda.moeda(p)} é {moeda.moeda(moeda.metade(p))}')