from lib.interface import *
from lib.arquivo import *

arq='cursoemvideo.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)


while True:
    resposta=menu(['Ver pessoas cadastradas','Adicionar uma nova pessoa','Sair do sistema'])
    if resposta == 1:
        #opçao listando um arquivo
        lerArquivo(arq)

    elif resposta == 2:
        #opçao inserindo pessoas
        cabeçalho('NOVO CADASTRO')
        nome=str(input('Nome: '))
        idade=leiaInt('Idade: ')
        cadastrar(arq,nome,idade)

    elif resposta == 3:
        print(linha())
        print('Você saiu do sistema'.center(50))
        print(linha())
        break
    else:
        print(linha())
        print('Escolha uma opção válida'.center(50))
        print(linha())
