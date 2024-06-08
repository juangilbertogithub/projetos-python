preco_espetaculo=float(input('Insira o preço do espetáculo: \nR$'))
preco_convite=float(input('Insira o valor do convite do espetáculo: \nR$'))

numero_convites=int(preco_espetaculo/preco_convite)
print(f'A quantidade de convites que devem ser vendidos para que pelo menos o custo do espetáculo seja alcançado deve ser de {numero_convites} bilhetes.')

preco_lucro=preco_espetaculo+preco_espetaculo*0.23
numero_convites_lucro=int(preco_lucro/preco_convite)
#ou lucro=1.23*espetaculo/convite
print(f'A quantidade de convites que devem ser vendidos para que se tenha um lucro de 23% deve ser de {numero_convites_lucro} bilhetes.')

#Faça um programa que receba o custo de um espetáculo teatral e o preço do convite desse espetáculo. Esse programa deve calcular e mostrar:
#a) A quantidade de convites que devem ser vendidos para que pelo menos o custo do espetáculo seja alcançado.
#b) A quantidade de convites que devem ser vendidos para que se tenha um lucro de 23%.