pessoa={'nome': 'Juan', 'idade':25}
pessoa=dict(nome='Juan', idade=25) #quivalente ao de cima
pessoa['telefone']='1234-5678' #adiciona no dicionario
print(pessoa)

dados={'nome': 'Juan', 'idade':25, 'telefone':'1234-5678'}
print(dados['nome']) #vai mostrar o dado referente ao q foi pedido qnd n ha atribuiçao
print(dados['idade'])
print(dados['telefone'])

dados['nome'] ='Maria' #vai mudar o dado por atribuir algo
dados['idade']=28
dados['telefone']='234567890'
print(dados)

contato={
    'juan@gmail.com':{'nome':'Juan','telefone':'12345678'}, #aninhando o dicionario
    'fabio@gmail.com':{'nome':'Fabio','telefone':'12345678'},
    'giovana@gmail.com':{'nome':'Giovana','telefone':'12345678','extra':{'a':1}},
}

telefone=contato['juan@gmail.com']['telefone'] #funciona parecido com um banco de dados. puxo algo de dentro do dicionario
print(telefone)

extra=contato['giovana@gmail.com']['extra']['a']
print(extra)

for chave in contato:
    print(chave, contato[chave])
for chave, valor in contato.items():
    print(chave,valor)

#metodos da classe dict

copia=contato.copy() #copia
print(f'Essa é uma cópia: {copia}')

copia.clear()
print(copia)

print(dict.fromkeys(['nome','telefone']))
print(dict.fromkeys(['nome','telefone'],'vazio'))

contatos={
    'juan@gmail.com':{'nome': 'Juan', 'telefone': '1234-5678'}
}

print(contatos.get('chave')) #retorna None por n existir
print(contatos.get('chave',{})) #retorna {} por n existir, mas inserir um valor default
print(contatos.get('juan@gmail.com',{})) #retorna completo sem modificar

print(contatos.items()) #bom pra usar com for ou iterar

print(contatos.keys())#mostra as chaves

"""print(contatos.pop('juan@gmail.com')) #deleta a chave e mostra qual foi deletada
print(contatos.pop('juan@gmail.com', 'nao encontrou')) #se n tiver nada vc pode por um valor pra retornar



contatos={
    'juan@gmail.com':{'nome': 'Juan', 'telefone': '1234-5678'}
}
contatos.popitem()
print(contatos)
contatos.popitem()
print(contatos)"""


contatos={
    'juan@gmail.com':{'nome': 'Juan', 'telefone': '1234-5678'}
}
#contatos.setdefault('nome','Giovana')
print(contatos)

contatos.setdefault('idade',25)
print(contatos)


contatos={
    'juan@gmail.com':{'nome': 'Juan', 'telefone': '1234-5678'}
}
contatos.update({'juan@gmail.com': {'nome':'Ju'}})
print(contatos)

contatos.update({'giovana@gmail.com': {'nome':'Giovana','telefone': '4321-9876'}})
print(contatos)

contato={
    'juan@gmail.com':{'nome':'Juan','telefone':'12345678'},
    'fabio@gmail.com':{'nome':'Fabio','telefone':'12345678'},
    'giovana@gmail.com':{'nome':'Giovana','telefone':'12345678'},
}

print(contato.values())

resultado='juan@gmail.com' in contato
print(resultado)
resultado='gilberto@gmail.com' in contato
print(resultado)
resultado='idade'in contato['juan@gmail.com']
print(resultado)
resultado='telefone'in contato ['juan@gmail.com']
print(resultado)

contato={
    'juan@gmail.com':{'nome':'Juan','telefone':'12345678'},
    'fabio@gmail.com':{'nome':'Fabio','telefone':'12345678'},
    'giovana@gmail.com':{'nome':'Giovana','telefone':'12345678'},
}

del contato['juan@gmail.com']['telefone']
print(contato)
del contato ['giovana@gmail.com']
print(contato)