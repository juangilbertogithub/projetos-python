def aumentar(preço=0,taxa1=0, formato=False):
    res=preço+(preço*taxa1/100)
    return res if formato is False else moeda(res)


def diminuir (preço=0,taxa2=0, formato=False):
    res=preço-(preço*taxa2/100)
    return res if formato is False else moeda(res)


def dobro(preço=0, formato=False):
    res=preço*2
    return res if formato is False else moeda(res)


def metade(preço=0, formato=False):
    res=preço/2
    return res if formato is False else moeda(res)


def moeda(preço=0,moeda='R$'):
    return f'{moeda}{preço:.2f}'.replace('.',',')


def resumo(preço=0,taxa1=0,taxa2=0):
    print('-'*50)
    print('RESUMO'.center(50))
    print('-' * 50)
    print(f'O preço é de {moeda(preço)}'.center(50))
    print('-' * 50)
    print(f'O valor aumentado em {taxa1}% é: {aumentar(preço,taxa1,True)}')
    print(f'O valor diminuido em {taxa2}% é: {diminuir(preço,taxa2,True)}')
    print(f'O dobro é: {dobro(preço,True)}')
    print(f'A metade é: {metade(preço,True)}')
    print('-' * 50)