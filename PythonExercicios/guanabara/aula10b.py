"""carro.siga()
if esquerda:
    1
    2
    3
else:
    a
    b
    c
print('Chegou.')

ou

print('x' if A else 'y')

nome=str(input('Insira seu nome: '))
if nome=='Juan':
    print('Que nome bonito!')
else:
    print('Nada a ver esse nome aí...')

print(f'Bom dia, boa tarde, boa noite, {nome}.')"""

n1=float(input('Digite a primeira nota: '))
n2=float(input('Digite a segunda nota: '))
media=(n1+n2)/2
if media>=6.0:
    print(f'Sua nota é {media:.1f}. Parabéns, você passou!')
else:
    print(f'Sua nota é {media:.1f}. Você não passou.')

#ou print('Você passou!' if media>=6.0 else 'Você não passou.')