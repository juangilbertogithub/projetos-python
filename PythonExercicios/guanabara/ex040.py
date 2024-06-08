n1=float(input('Digite a sua primeira nota: '))
n2=float(input('Digite a sua segunda nota: '))
media=(n1+n2)/2

if media<5:
    print('REPROVADO')
elif 5>=media<7:
    print('RECUPERAÇÃO')
elif media>=7:
    print('APROVADO')

print(f'Sua média foi de {media:.1f}.')