nome=str(input('Qual o seu nome?\n')).strip().capitalize()
nome2=nome.upper()
if nome2=='JUAN':
    print('Que nome bonito!')
elif nome2=='PEDRO' or nome2=='ROBERTO':
    print('Que nome popular!')
elif nome2 in 'PAULA FERNANDA CARLA':
    print('Que nome feminino.')
else:
    print('Seu nome é muito normal.')
print(f'Tenha um bom dia, {nome}.')