from datetime import datetime

dados={}

dados['nome']=str(input('Insira seu nome: ')).strip().capitalize()
ano_de_nascimento=int(input('Ano de nascimento: '))
dados['idade'] = datetime.now().year - ano_de_nascimento #importante
dados['ctps']=int(input('Carteira de trabalho (Insira 0 se não tem): ')) #fazer lista com dicionario
if dados['ctps']!=0:
    dados['contrataçao']=int(input('Ano de contratação: '))
    dados['salario']=float(input('Insira o seu salário: '))
    dados['aposentadoria'] = dados['idade'] + dados['contrataçao'] + 35 - datetime.now().year

for k,v in dados.items():
    print(f'- {k} tem o valor {v}.')