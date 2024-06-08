peso=float(input('Digite seu peso: '))
altura=float(input('Digite a sua altura (em metros): '))
imc=peso/(altura**2)
if imc < 18.5:
    print(f'Seu IMC é {imc:.1f}. Você está abaixo do peso.')
elif imc < 25:
    print(f'Seu IMC é {imc:.1f}. Você está no peso ideal.')
elif imc < 30:
    print(f'Seu IMC é {imc:.1f}. Você está no sobrepeso.')
elif imc <40:
    print(f'Seu IMC é {imc:.1f}. Você está obeso.')
else:
    print(f'Seu IMC é {imc:.1f}. Você está com obesidade mórbida.')