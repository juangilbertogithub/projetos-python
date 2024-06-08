carro=int(input('Quantos dias ficou com o carro? \n'))
km=float(input('Quanto quilômetros foram rodados? \n'))
carro2=carro*60
km2=km*0.15
total=carro2+km2
print(f'Será necessário pagar um total de R${total:.2f}.')