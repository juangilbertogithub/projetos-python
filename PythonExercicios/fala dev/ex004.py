from math import ceil

largura=float(input('Insira a largura: '))
altura=float(input('Insira a altura: '))
area=largura*altura
litros_cobrir=area/3
latas=ceil(litros_cobrir/18)
print(f'A área pintada será de {area:.2f}m².')
print(f'A quantidade de tinta para cobrir a área é de {litros_cobrir:.1f}l.')
print(f'Serão necessárias {latas} latas para pintar. O total é de R${latas*80:.2f}.')


#1l->3m^2
#xl->area
1#lata->18 litros->80reais

#Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
# Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de
# 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.