dados=dict()
dados['nome']=str(input('Nome: ')).capitalize().strip()
dados['media']=float(input(f'Média de {dados["nome"]}: '))
"""print(f'Aluno: {dados["nome"]}\nMédia: {dados["media"]}')
print('Situação: ', end='')"""
if dados['media'] >= 6:
    dados['situaçao']='APROVADO'
else:
    dados['situaçao']='APROVADO'

print(dados['situaçao'])

for k,v in dados.items():
    print(f'{k} é igual a {v}.')