n1=int(input('Insira o primeiro valor: '))
n2=int(input('Insira o segundo valor: '))
lista=(n1,n2)
escolha=0
print()
while escolha!=5:
    print('''MENU
[1] Somar
[2] Multiplicar
[3] Maior
[4] Novos números
[5] Sair do programa''')
    print()
    escolha = int(input('Escolha um valor: '))
    print()
    if escolha == 1:
        print(f'{n1} + {n2} = {n1 + n2}')
        print()
    elif escolha == 2:
        print(f'{n1} x {n2} = {n1 * n2}')
        print()
    elif escolha == 3:
        print(f'O maior número é o {max(lista)}.')
        print()
    elif escolha == 4:
        n1 = int(input('Insira um novo primeiro valor: '))
        n2 = int(input('Insira um novo segundo valor: '))
        lista = (n1,n2)
        print()
    elif escolha == 5:
        print('Você saiu do programa.')
        print()
    elif escolha >= 6:
        print('Valor inválido. Por favor, escolha uma opção.')
        print()

print('Obrigado por utilizar.')