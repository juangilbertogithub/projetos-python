resposta=str(input('Deseja continuar? Sim ou Não: '))[0].upper().strip()
while resposta!='S' and resposta!='N':
    print('Valor inválido!')
    resposta = str(input('Deseja continuar? Sim ou Não: '))[0].upper().strip()
    while resposta=='S':
        resposta=str(input('Deseja continuar? Sim ou Não: '))[0].upper().strip()
print('Finalizado.')

#Escreva o trecho de um programa que lê e valida a resposta da seguinte pergunta: “Deseja continuar (s/n)?