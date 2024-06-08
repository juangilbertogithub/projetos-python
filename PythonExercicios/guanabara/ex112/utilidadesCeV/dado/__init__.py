def leiaDinheiro(msg):
    valido=False
    while not valido:
        entrada=str(input(msg)).replace(',','.').strip()
        if entrada.isalpha() or entrada=='':
            print(f'Erro!\n"{entrada}" é inválido.')
        else:
            valido=True
            return float(entrada)


def leiaint(msg):
    ok=False
    valor=0
    while True:
        n=str(input(msg))
        if n.isnumeric():
            valor=int(n)
            ok=True
        else:
            print('Erro! Esse valor não é um número.')
        if ok:
            break

