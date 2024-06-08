times=('Botafogo', 'Palmeiras', 'Flamengo', 'Fluminense', 'São Paulo',
       'Fortaleza','Cruzeiro','Fortaleza', 'Vasco','Bahia')

print(f'Os time são {times}.')
print(f'Os 5 primeiros colocados são: {times[0:5]}.')
print(f'Os últimos 4 colocados são: {times[-4:]}') #ou {times[-1]}, {times[-2]}, {times[-3]} e {times[-4]}.
print(f'Os times em ordem alfabética: {sorted(times)}')
print(f'O Fluminense está na posição {times.index("Fluminense")+1}.')