cedula50=0
cedula20=0
cedula10=0
resto=0

valor=int(input('Insira um valor: '))
while True:
    if valor>=50: #errei aqui colocando porcentagem
        valor-=50
        cedula50+=1
    else:
        if valor >=20:
            valor-=20
            cedula20+=1
        else:
            if valor >=10:
                valor-=10
                cedula10+=1
            else:
                resto=valor
                break



"""    while valor%20!=0:
        valor-=20
        cedula20+=1
        break
        while valor%10!=0:
            valor-=20
            cedula10+=1
            resto=valor
            break"""

print(f'Você sacou {cedula50} cédulas de 50 reais, {cedula20} cédulas de 20 reais, {cedula10} cédulas de 10 reais e {resto} cédulas de 1 real.')