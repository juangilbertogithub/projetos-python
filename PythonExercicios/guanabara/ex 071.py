#pega o valor total e divide por 50. pego o resto. divido por 20. pego o resto. vou pegando o resto e usando pra dividir com os valores de cedulas. while nao for 1 ele n para de contar esses bloquinhos diferentes.
#possoo contar as cedulas
"""dinheiro=int(input('''Quanto gostaria de sacar?
R$: '''))

notas50=dinheiro//50
dinheiroresto50=dinheiro%50

notas20=dinheiroresto50//20
dinheiroresto20=dinheiroresto50%20

notas10=dinheiroresto20//10
dinheiroresto10= dinheiroresto20%10

notas1= dinheiroresto10

if notas50 or notas20 or notas10 or notas1 ==0:
    print('')

print(dinheiro,
      notas50,
      notas20,
      notas10,
      notas1)"""

"""valor=int(input('Quanto quer sacar? '))
total=valor
ced=50
totalced = 0

while True:
    if total>=ced:
        total-=ced
        totalced+=1
    else:
        if totalced > 0:
            print(f'Total de {totalced} cédulas de R${ced}')
        if ced == 50:
            ced = 20
        elif ced ==20:
            ced=10
        elif ced == 10:
            ced=1
        if total == 0:
            break"""

lista = [50, 20, 10, 1]
valor = int(input('Insira o valor que desaja sacar R$ '))
total = valor # para manter a variável VALOR com o dado inserido pelo usuário
cont = 0
while True:
    if total >= lista[cont]:
        nota = total // lista[cont]
        print(f'Total de {nota} notas de R$ {lista[cont]}')
        total = total % lista[cont]
    cont += 1
    if total == 0:
        break

cont