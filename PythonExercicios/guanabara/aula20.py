def mostraLinha():
    print('-'*30)


mostraLinha()
print('Oi')
mostraLinha()
mostraLinha()
print('Tudo bem?')
mostraLinha()

print()


def mensagem(msg):
    print('-'*30)
    print(msg)
    print('-'*30)


mensagem('oi')


#programa de soma
def soma(a,b):
    s=a+b
    print(s)


soma(1,2)
soma(a=3,b=4) #posso deixar explicito
soma(b=5,a=6) #posso mudar a ordem


def soma(a,b):
    print(f'A = {a} e B = {b}')
    s=a+b
    print(f'A soma de {a} + {b} = {s}')


soma(1,2)
soma(a=3,b=4) #posso deixar explicito
soma(b=5,a=6) #posso mudar a ordem


def contador(*num):
    print(num)


contador(5,2,3)
contador(1,5,6,2)
contador(2,1)


def contador(*num):
    for valor in num:
        print(f'{valor}', end=' ')
    print()


contador(5,2,3)
contador(1,5,6,2)
contador(2,1)


def contador(*num):
    tam=len(num)
    print(f'Recebi os valores {num} e são ao todo {tam} números.')


contador(5,2,3)
contador(1,5,6,2)
contador(2,1)


valores=[7,2,5,0,4]
def dobra(lst): #n é um empacotamento
    pos=0 #começa na posiçao 0
    while pos<len(lst): #enquanto a posiçao for menor que a quantidade da lista
        lst[pos]*=2 #pega o valor da lista e multiplica por dois. td oq eu fizer no lst, ira influenciar no valor
        pos+=1 #passa pra proxima
dobra(valores)
print(valores)

def soma (*valores):
    s=0
    for num in valores:
        s+=num
    print(f'Somando os valores {valores} temos {s}.')

soma(5,2)
soma(2,9,4)