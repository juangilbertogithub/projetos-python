def leiaInt(msg):
    while True:
        try:
            n=int(input(msg))
        except:
            print(linha())
            print('Escolha uma opção válida'.center(50))
            print(linha())
            continue
        else:
            return n


def linha ():
   return('-'*50)


def cabeçalho (txt):
    print(linha())
    print(txt.center(50))
    print(linha())
    return


def menu(lista):
    cabeçalho('MENU PRINCIPAL')
    c=1
    for item in lista:
        print(f'{c} - {item}')
        c+=1
    print(linha())
    opçao=leiaInt('Sua opção: ')
    return opçao