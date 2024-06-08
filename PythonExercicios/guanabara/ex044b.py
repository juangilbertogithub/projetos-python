valor=float(input('Digite o valor do seu produto: '))
escolha1=int(input('''1- Dinheiro/Cheque
2- Cartão
Escolha a forma de pagamento: '''))

if escolha1 == 1:
    desconto=valor-(valor*0.1)
    print(f'O valor do seu produto custa R${valor:.2f}. Com o desconto de 10% sairá por R${desconto:.2f}')
elif escolha1 == 2:
    escolha2=int(input('''1- À vista
2- 2x
3- 3x ou mais
Como irá pagar? '''))
    if escolha2 == 1:
        desconto=valor-(valor*0.05)
        print(f'O valor do seu produto custa R${valor:.2f}. Com o desconto de 5% sairá por R${desconto:.2f}')
    elif escolha2 == 2:
        print(f'O valor do seu produto custa R${valor:.2f}. Não há desconto, logo, sairá pelo mesmo valor.')
    elif escolha2 == 3:
        juros=valor+(valor*0.2)
        print(f'O valor do seu produto custa R${valor:.2f}. Com o juros de 20% sairá por R${juros:.2f}')
else:
    print('Opção inválida. Tente novamente.')