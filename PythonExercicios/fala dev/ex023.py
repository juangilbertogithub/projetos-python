from time import sleep
"""print('Contagem regressiva para o lançamento de um foguete')
for c in range(10,-1,-1):
    print(c,end=' ')
    sleep(1)
print()
print('Fogo!')"""

#outra maneira

contagem=10
while contagem > -1:
    print(contagem,end=' ')
    contagem-=1
    sleep(1)
print()
print('Fogo!')

#Escreva um programa para escrever na tela a contagem regressiva do lançamento de um foguete. O programa deve exibir 10, 9, 8, ..., 1,0 e Fogo!