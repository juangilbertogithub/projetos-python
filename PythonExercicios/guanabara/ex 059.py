n1=int(input('Primeiro valor: '))
n2=int(input('Segundo valor: '))

opçao=0

while opçao!=5:
    opçao=int(input('''
    1- Somar
    2- Multiplicar
    3- Maior
    4- Novos números
    5- Sair
    
Escolha uma opção: '''))
    if opçao==1:
        soma=n1+n2
        print(f'\nA soma de {n1} e {n2} é {soma}.')
    elif opçao==2:
        multiplicaçao=n1*n2
        print(f'\nA multiplicação de {n1} e {n2} é {multiplicaçao}.')
    elif opçao==3:
        if n1>n2:
            print(f'\nO maior número entre os valores {n1} e {n2} é {n1}.')
        if n2>n1:
            print(f'\nO maior número entre os valores {n1} e {n2} é {n2}.')
        if n1==n2:
            print('\nOs valores são iguais. Não existe um maior.')
    elif opçao==4:
        print('\nInsira novos valores')
        n1=int(input('Primeiro valor: '))
        n2=int(input('Segundo valor: '))
    elif opçao==5:
        print('\nVocê saiu do programa.')
    else:
        print('\nEsta opção não existe. Por favor, insira um novo valor.')