v=int(input('Qual a sua velocidade? '))

if v>80:
    multa=(v-80)*7
    print(f'Você está acima da velocidade. Você foi multado em R${multa}.')

else: #nem precisa do else nesse caso
    print('Boa viagem')