km=float(input('Insira a quantidade de Km percorridos: '))
dias=int(input('Insira a quantidade de dias: '))
total=(60*dias)+(0.15*km)
print(f'Você percorreu {km:.1f} Km e utilizou o carro por {dias} dias. O total a ser pago é de R${total:.2f}.')