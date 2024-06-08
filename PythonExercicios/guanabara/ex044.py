valor=float(input('Digite o valor do seu produto: '))

condiçao=int(input("""
1)Dinheiro/Cheque (à vista)
2)Cartão (à vista)
3)2x no cartão
4)3x ou mais no cartão
Digite a sua opção de pagamento: """))

if condiçao==1:
    print(f"""Você escolheu Dinheiro/Cheque (à vista).
    Seu produto custa R${valor-(valor*10/100):.2f} (10% de desconto).""")
if condiçao==2:
    print(f"""Você escolheu Cartão (à vista).
        Seu produto custa R${valor-(valor * 5 / 100):.2f} (5% de desconto).""")
if condiçao==3:
    print(f"""Você escolheu 2x no cartão.
            Seu produto custa R${valor:.2f} (sem juros).""")
if condiçao==4:
    parcela=int(input('Em quantas parcelas? '))
    print(f"""Você escolheu 3x ou mais no cartão.
                Seu produto será pago em {parcela}x e custa R${(valor*20/100)+valor:.2f} (20% de juros).""")
else:
    print('Tente novamente. Digite uma das opções.')