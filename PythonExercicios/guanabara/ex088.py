from random import randint
from time import sleep

jogo=list()
lista_numeros=list()

contagem=0
total=1
numero_sorteios=int(input('Quer que eu sorteie quantos jogos? '))
print('Boa sorte!')
sleep(1)

while total <= numero_sorteios:
    contagem=0
    #print(f'Jogo {contagem1}: ', end='')

    while True:
        dados=randint(1,60)
        if dados not in lista_numeros:
            lista_numeros.append(dados)
            contagem+=1
        if contagem>=6:
            break

    lista_numeros.sort()
    jogo.append(lista_numeros[:])
    lista_numeros.clear()
    total+=1

for c,v in enumerate(jogo):
    print(f'Jogo {c+1}: {v}')
    sleep(0.5)

print('Fim do sorteio.')