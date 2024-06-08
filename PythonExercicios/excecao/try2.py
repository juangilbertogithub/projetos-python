try:
    a=[]
    print(a[1])
except NameError as erro:
    print('Erro do desenvolvedor')
except IndexError as erro:
    print('Erro de índice')
except Exception as erro:
    print('Ocorre um erro inesperado')

try:
    a={}
    print(a[1])
except NameError as erro:
    print('Erro do desenvolvedor')
except (IndexError, KeyError):
    print('Erro de índice ou chave')
except Exception as erro:
    print('Ocorre um erro inesperado')
else:
    print('Código executado com sucesso!')
    print(a)
    #pass
finally:
    print('Finalmente.')
print('Continuando...')

try:
    a=1/0
except NameError as erro:
    print('Erro do desenvolvedor')
except (IndexError, KeyError):
    print('Erro de índice ou chave')
except Exception as erro:
    print('Ocorre um erro inesperado')
else:
    pass
finally:
    a='Oi'
print(a)