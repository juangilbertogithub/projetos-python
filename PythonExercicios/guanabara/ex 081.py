resp=''
lista=[]

while True:
    lista.append(int(input('Digite um valor: ')))

    resp=str(input('Deseja continuar [Sim/Não]? ')).capitalize()[0]
    if resp == 'N':
        break
    if resp!='S':
        print('Esse valor não existe. Por favor, tente novamente')

print(f'Foram digitados {len(lista)} valores na sua lista.')
lista.sort(reverse=True)
print(f'Os valores em ordem decrescente são {lista}')
print(f'O valor "5" foi digitado e está lista.') if 5 in lista else print('O valor "5" não foi digitado.')