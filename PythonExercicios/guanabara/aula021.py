help(input)
print(input.__doc__)


def contador(i,f,p):
    """
    Faz contagem e mostra na tela.
    :param i: início da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    :return: sem retorno
    Função criada por mim.
    """
    c=i
    while c<=f:
        print(f'{c}',end='.. ')
        c+=p
    print('FIM!')


help(contador)


def somar(a,b,c=0):
    s=a+b+c
    print(f'A soma vale {s}.')

somar(8,5,4)
somar(8,4)


def somar(a=0,b=0,c=0):
    s=a+b+c
    print(f'A soma vale {s}.')

somar()
somar(a=4,b=5)
somar(c=3,b=1)


def teste():
    x=8 #escopo local
    print(f'No programa principal, n vale {n}.')
    print(f'No programa principal, x vale {x}.')


n=2 #escopo global
print(f'No programa principal, n vale {n}.')
teste()
#print(f'No programa principal, x vale {x}.') #ela so existe declarada dentro do teste, entao n ira funcionar fora do teste.


def teste(b):
    b+=4
    c=2
    print(f'A dentro vale {a}.')
    print(f'B dentro vale {b}.')
    print(f'C dentro vale {c}.')

a=5
teste(a)
print(f'A fora vale {a}.')
#print(f'B fora vale {b}.') nao funciona
#print(f'C fora vale {c}.') nao funciona


def teste(b):
    a=8 #apesar de ter variavel igual a local, aparecera o valor local no print. n ira ser afetado
    b+=4
    c=2
    print(f'A dentro vale {a}.')
    print(f'B dentro vale {b}.')
    print(f'C dentro vale {c}.')

a=5
teste(a)
print(f'A fora vale {a}.')


def teste(b):
    global a #declarando q a variavel de fora é global, ele usara o valor global
    a=8
    b+=4
    c=2
    print(f'A dentro vale {a}.')
    print(f'B dentro vale {b}.')
    print(f'C dentro vale {c}.')

a=5
teste(a)
print(f'A fora vale {a}.')


def somar(a=0,b=0,c=0):
    s=a+b+c
    return s #funciona como o break no def

#print(somar(1,2,3)) tambem posso usar dessa forma
r1=somar(1,2,3) #tambem posso dar um print direto
r2=somar(1,2)
r3=somar(1)

print(f'Os meus cálculos deram {r3},{r2},{r1}.')



def fatorial(num=1):
    f=1
    for c in range(num,0,-1):
        f*=c
    return f


n=int(input('Digite um fatorial: '))
print(f'O fatorial de {n} é {fatorial(n)}.')

f1=fatorial(5)
f2=fatorial(3)
f3=fatorial()

print(f'O resultado é {f1}, {f2} e {f3}.')


def parouimpar(n=0):
    if n % 2 == 0:
        return True
    else:
        return False

num=int(input('Insira um valor: '))
print(parouimpar(num))

if parouimpar(num):
    print('É par!')
else:
    print('Não é par!')