lista=('Lápis', 1, 'Borracha', 2, 'Caneta', 3, 'Corretivo', 4)

print('-'*50)
print(f'{"TABELA DE COMPRAS":^50}')
print('-'*50)

contpar=0
contimpar=1

while contimpar < len(lista):

    print(f'{lista[contpar]:.<40}',f'R${lista[contimpar]:>5.2f}')
    contpar+=2
    contimpar += 2

print('-'*50)


"""print(54*'-')
print(15*' ', 'LISTAGEM DE PREÇOS')
print(54*'-')
lista = ('Lápis', 1.75, 'Borracha', 2.00, 'Caneta', 1.20, 'Caderno', 7.50, 'Lapiseira', 1.99)
for i in range(0, 10, 2):
    j = i + 1
    pontinhos = (44-len(lista[i]))*'.'
    print(f'{lista[i]} {pontinhos} R$ {lista[j]:>.2f}')
print(54*'-')"""

"""produtos = ("Lápis", 1.75, "Borracha", 2.00, "Caderno", 15.90, "Estojo", 25.00, "Transferidor", 4.20,
            "Compasso", 9.99, "Mochila", 120.32, "Canetas", 22.30, "Livro", 34.90)

print("="*50)
print("{:^50}".format("LISTAGEM DE PREÇOS"))
print("="*50)

for c in range(0, len(produtos), 2):
    print(f"{produtos[c]:.<40}", f" R$ {produtos[c+1]:>7.2f}")

print("="*50)"""