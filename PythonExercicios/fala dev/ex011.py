print('Conversor REAL -> DÓLAR')
real=float(input('Insira o valor em Real: R$'))
cotacao_atual=float(input('Insira a cotação atual do Dolar: $'))
dolar=real/cotacao_atual
print(f'Valor convertido: ${dolar:.2f}')

#Receba a quantidade de dinheiro, em reais, que uma pessoa tem para fazer uma viagem ao exterior. Receba, também, o valor
#da cotação do dólar do dia. Calcule e apresente o valor convertido em dólares.