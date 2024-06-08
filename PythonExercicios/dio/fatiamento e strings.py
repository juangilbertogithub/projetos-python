curso='   PyThOn '

print(curso.upper())
print(curso.lower())
print(curso.title())
print(curso.strip())

print(curso.center(10,'#')) # ou print('##'+curso+'##')
print(curso.center(10))
print('.'.join(curso))
print(curso+'.')

for letra in curso:
    print(letra,end='-') #claro, colocando uma numeraçao pra dar um break ou indicar quando chegou na ultima letra

nome='Juan'
idade=25
saldo=45.435
print(f'Seu nome é {nome} e tem {idade} anos. Seu saldo é de R${saldo:.2f}. Seu saldo é de R${saldo:10.2f}.')

nome='Juan Gilberto'
print(nome[0]) #letra especifica
print(nome[:7]) #de começo a 7
print(nome[3:]) #de 3 pra frente
print(nome[3:7]) #inicio e fim especifico
print(nome[1:8:2]) #pulando de dois em dois
print(nome[:]) #completp
print(nome[::-1])#espelhado

mensagem=f"""Olá, meu nome é {nome}.
Eu estou aprendendo Pyhon."""
print(mensagem)
#ou
print(f'''  Olá, meu nome é {nome}.
Eu estou aprendendo Pyhon.''')

print(
    '''
    =====MENU=====
    
    1-Depositar
    2-Sacar
    0-Sair
    
    ==============
Obrigado por utilizar!!!'''
)