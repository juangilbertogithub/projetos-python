print('-------')
print('-------')
print('-------')
print('-------')
print('-------')
print('-------')

print()

def mostraLinha(): #n executa a def. apenas qnd vc chama ela
    print('-------')

mostraLinha() #toda vez que uso o mostra linha ele vai ate o meu def e depois avança pra proxima coisa
print('oi')
mostraLinha()
print('tudo bom?')


def mensagem (msg):
    print('-------')
    print(msg)
    print('-------')

mensagem('oi')
mensagem('tudo bem?') #escreve naquele espaço vazio que defini



def soma(a,b):
    s=a+b
    print(s)

soma(4,5)
soma(b=5,a=4)

def soma(a,b):
    print(f'A = {a} e B = {b}')
    s=a+b
    print(f'A soma A + B = {s}')

soma(4,5)
