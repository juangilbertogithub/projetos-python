largura=float(input('Largura da parede (em metros): '))
altura=float(input('Altura da parede (em metros): '))
area=largura*altura
print(f'Sua parede tem a dimensão de {largura:.2f}x{altura:.2f} e sua área é de {area:.2f}m².')
tinta=area/2
print(f'Para pintar a parede você precisará de {tinta:.2f}l de tinta.')