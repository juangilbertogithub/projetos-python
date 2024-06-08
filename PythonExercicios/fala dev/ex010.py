ano=int(input('Digite um ano (de quatro dígitos): '))
if ano%4==0 and ano%100!=0 or ano%400==0:
    print(f'{ano} é bissexto.')
else:
    print(f'{ano} não é bissexto.')

#Faça um programa que receba um ano (quatro dígitos) e informe se é um ano bissexto ou não. Pesquise quais as regras para o número ser bissexto.