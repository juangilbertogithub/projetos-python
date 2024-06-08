while True:
    n=int(input('Digite um valor para a tabuada (valor negativo para sair): '))
    if n <0:
        print('Tabuada encerrada.')
        break
    else: #nao precisa
        for c in range (1,11):
            print(f'{n} x {c} = {n*c}')
