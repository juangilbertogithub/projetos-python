""""\033[0;30;41m]
\033[4;33;44m]
\033[1;35;43m]
\033[30;42m]
\033[m
\033[7:3;m]"""

"""print('\033[1;31;43mOlá,Mundo!\033[m') #em negrito, vermelho, fundo amarelo, limitando o tamanho até o fim do texto"""

"""nome='Juan'
cores= {'limpa': '\033[m',
        'azul': '\033[34m',
        'amarelo': '\033[33m',
        'pretoebranco': '\033[7;30m'}
print(f'Olá, {cores["azul"],nome,cores["limpa"]}!')"""

nome = 'Juan'
cores = {'limpa': '\033[m',
         'azul': '\033[34m',
         'amarelo': '\033[33m',
         'pretoebranco': '\033[7:30m'}
print(f'Olá! Muito prazer em te conhecer, {(cores["amarelo"])}{nome:}!!!')