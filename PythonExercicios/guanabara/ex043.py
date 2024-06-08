from time import sleep

print('Descubra o seu IMC \n')

sleep(1)

peso=float(input('Digite o seu peso: '))
altura=float(input('Digite a sua altura: '))

imc=peso/(altura**2)

sleep(1)

print(f'Seu IMC é de {imc:.1f}.')

if imc<=18.5:
    print('Você está abaixo do peso.')
if 18.5<imc<=25:
    print('Você está no peso ideal.')
if 25<imc<=30:
    print('Você está com sobrepeso.')
if 30<imc<=40:
    print('Você está obeso.')
else:
    print('Você está com obesidade morbida.')