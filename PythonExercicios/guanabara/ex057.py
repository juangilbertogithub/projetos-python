sexo=str(input('Digite seu sexo [M/F]: ')).upper().strip()[0] #pra pegar somente a primeira letra (fatiamento)

while sexo not in 'MmFf': #esqueci de colocar a palavra sexo e foi util colocar o in
    print('Inválido')
    sexo = str(input('Digite novamente o seu sexo [M/F]: ')).upper().strip()

print('Correto')
print('FIM')