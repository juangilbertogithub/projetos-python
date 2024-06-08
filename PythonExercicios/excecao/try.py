try:
    print(x)
except:
    print('Erro no programa')
else:
    print('Tudo certo')

x=10
#apenas try e except sao obrigatorios no tratamento de erros
try: #mostre
    print(x)
except: #se der erro
    print('Erro no programa')
else: #caso n gere um erro
    print('Tudo certo')
finally: #independente se deu certo ou nao, mostre no final
    print('fim do tratamento')

num=10
if num<1:
    raise Exception('Valor não permitido.') #permite uma mensagem personalizada do erro

num='a'
if not type(num) is int:
    raise Exception('Somente números permitidos')
else:print(num)