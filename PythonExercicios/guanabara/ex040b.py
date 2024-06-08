n1=float(input('Digite a sua primeira nota: '))
n2=float(input('Digite a sua segunda nota: '))
media=(n1+n2)/2
if media < 5:
    print(f'Sua nota foi {media:.1f}.')
    print('REPROVADO')

if media>=5 and media<7: #ou if 5>= media <7:
    print(f'Sua nota foi {media:.1f}.')
    print('RECUPERAÇÃO')

if media>=7:
    print(f'Sua nota foi {media:.1f}.')
    print('APROVADO')