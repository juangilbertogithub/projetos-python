from moeda import * #maneira 1

p=float(input('Digite o preço: R$'))

print(f'O valor aumentado em 10% de {moeda(p)} é {moeda(aumentar(p,10,True))}')
print(f'O valor diminuido em 13% de {moeda(p)} é {moeda(diminuir(p,13,True))}')
print(f'O dobro de {moeda(p)} é {moeda(dobro(p,True))}')
print(f'A metade de {moeda(p)} é {moeda(metade(p,True))}')


"""import moeda #maneira 2

p=float(input('Digite o preço: R$'))

print(f'O valor aumentado em 10% de {moeda.moeda(p)} é {moeda.aumentar(p,10,True)}')
print(f'O valor diminuido em 13% de {moeda.moeda(p)} é {moeda.diminuir(p,13,True)}')
print(f'O dobro de {moeda.moeda(p)} é {moeda.dobro(p,True)}')
print(f'A metade de {moeda.moeda(p)} é {moeda.metade(p,True)}')"""