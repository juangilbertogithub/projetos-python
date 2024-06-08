lista=[]

while True:
    lista.append(int(input('Insira um valor: ')))

    pergunta=str(input('Deseja continuar? Sim ou Não: ')).strip().upper()[0]
    if pergunta == 'N':
        break

print(f'Foram digitados {len(lista)} números.')

lista.sort(reverse=True)
print(f'A lista em ordem decrescente fica {lista}.')

if 5 in lista:
    print(f'Há o número 5 na lista. Ele está na posição {lista.index(5)+1}.')
else:
    print('Não há o número 5 na lista.')

print('FIM')