def exibir_mensagem():
    print('Olá mundo!')

def exibir_mensagem_2(nome):
    print(f'Seja bem vindo {nome}!')

def exibir_mensagem_3 (nome='Anônimo'):
    print(f'Seja bem vindo {nome}!')

exibir_mensagem()
exibir_mensagem_2(nome='Juan') # ou ('Juan') apenas. se n tivesse o nome daria erro
exibir_mensagem_3() #o nome ja ta definido com um valor
exibir_mensagem_3(nome='Fabio') #se coloco um nome ele substitui


def calcular_total(numeros):
    return sum(numeros)

def retorna_antecessor_e_sucessor (numero):
    antecessor=numero-1
    sucessor=numero+1
    return antecessor,sucessor

print(calcular_total([10,20,34]))
print(retorna_antecessor_e_sucessor(10)) #retornou numa tupla pq é uma estrutura imutavel

def func_3():
    print('Olá mundo!') #sem isso ele retorna None
    return
print(func_3())

def salvar_carro(marca,modelo,ano,placa): #salva carro no banco de dados
    print(f'Carro inserido com sucesso! {marca}/{modelo}/{ano}/{placa}')
#posso fazer de tres formas diferentes
salvar_carro('Fiat','Palio','1999','ABC-1234') #a desvantagem dessa forma é q o cliente pode trocar a ordem sem querer
#salvar_carro(marca='Fiat',modelo='Palio', ano=1999, placa='ABC-1234') #a vantagem é q fica claro oq vai ser preenchido
#salvar_carro(**{'marca':'Fiat','modelo':'Palio','ano':1999,'placa':'ABC-1234'}) #o ** indica que estou passando um dicionario pra aquela funçao


# def f (pos1,pos2,/pos_or_kwd,*,kwd1,kwd2): apenas posiçao, posiçao ou chave, apenas chave

def criar_carro (modelo,ano,placa,/,marca,motor,combustivel): #posiçao apenas
    print(modelo,ano,placa,marca,motor,combustivel)

criar_carro('Palio',1999,'ABC-1234',marca='Fiat',motor='1.0',combustivel='Gasolina') #valido

#criar_carro(modelo='Palio',ano=1999,placa='ABC-1234',marca='Fiat',motor='1.0', combustivel='Gasolina') #invalido devido as coisas antes da barra que obriga a ser apenas por posiçao. é parametro por posiçao, n por nome

def criar_carro (modelo,ano,placa,/,*,marca,motor,combustivel): #letra e posiçao apenas
    print(modelo,ano,placa,marca,motor,combustivel)

criar_carro('Palio',1999,'ABC-1234',marca='Fiat',motor='1.0',combustivel='Gasolina') #valido

#criar_carro(modelo='Palio',ano=1999,placa='ABC-1234',marca='Fiat',motor='1.0', combustivel='Gasolina') #invalido

def criar_carro (modelo,ano,placa,/,marca,*,motor,combustivel): #marca por posiçao ou nome
    print(modelo,ano,placa,marca,motor,combustivel)

criar_carro('Palio',1999,'ABC-1234','Fiat',motor='1.0',combustivel='Gasolina') #valido

#criar_carro(modelo='Palio',ano=1999,placa='ABC-1234',marca='Fiat',motor='1.0', combustivel='Gasolina')

def somar(a,b):
    return a + b

def subtrair(a,b):
    return a - b

def exibir_resultado(a,b,funçao):
        resultado=funçao(a,b)
        print(f'O resultado da operação é {resultado}')

exibir_resultado(10,10,somar)
exibir_resultado(10,10,subtrair)

op=somar
print(op(1,23))

"""salario=2000
def salario_bonus:
    global salario #sem isso n funciona pq n tenho um valor salario inicial declarado
    salario+=bonus
    return salario
salario_com_bonus=salario_bonus(500) #2500
print(salario_com_bonus)"""

salario=2000
def salario_bonus(bonus,lista):
    global salario #sem isso n funciona pq n tenho um valor salario inicial declarado

    lista_aux=lista.copy()
    lista_aux.append(2)
    print(f'lista aux={lista_aux}')

    salario+=bonus
    return salario

lista=[1]
salario_com_bonus = salario_bonus(500,lista) #2500
print(salario_com_bonus)
print(lista)

