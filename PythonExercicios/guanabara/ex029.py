v=float(input('Digite a sua velocidade: '))
if v>80:
    multa=(v-80)*7
    print(f'Você ultrapassou o limite de velocidade (80km/h). Você deverá pagar uma multa de R${multa:.2f}.')
print('Tenha um bom dia e dirija com segurança!')