import moeda

p=float(input('Digite o preço: R$'))

print(f'O valor aumentado em 10% de {p} é {moeda.aumentar(p, 10)}')
print(f'O valor diminuido em 13% de {p} é {moeda.diminuir(p, 13)}')
print(f'O dobro de {p} é {moeda.dobro(p)}')
print(f'A metade de {p} é {moeda.metade(p)}')