km=float(input('Digite a quantidade de km rodados: '))
dias=int(input('Digite a quantidade de dias do aluguel: '))
preço=dias*60+km*0.15
print(f'O valor a ser pago é de R${preço:.2f}.')

#Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado pelo usuário, assim como a quantidade
#de dias pelos quais o carro foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$ 60,00 por dia e R$ 0,15 por km rodado.