cidade=str(input('Digite o nome de uma cidade: ')).strip()
cidademaiuscula=cidade.upper().split()
#print(cidademaiuscula[0].find('SANTO'))
print(f'Existe a palavra "Santo" no começo do nome da cidade {cidade}?')
print('SANTO' in cidademaiuscula[0]) #ou print(cidademaiuscula[0] == 'SANTO')