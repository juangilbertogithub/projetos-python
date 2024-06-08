nome=str(input('Digite seu nome completo: ')).strip()

print(nome.upper())

print(nome.lower())

nome.replace(' ','')
print(len(nome))
#ou len(nome) - nome.count(' '))

nomedividido=nome.split()
print(len(nomedividido[0]))
#ou nome.find(' ')