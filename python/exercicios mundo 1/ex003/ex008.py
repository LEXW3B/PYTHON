#faça um programa que mostre o calculo pra pintar uma parede dando o resultado da area da parede e o tanto de tinta gasto sendo que um litro de tinta pinta 2 m².
largura = float(input('Largura da parede: '))
altura = float(input('Altura da parede: '))
area = altura * largura
print('para pintar essa parede, voce precisara de {} x {} e a sua area e de {} m². '.format(altura, largura, area))
tinta = area / 2
print('para pintar eessa parede voce precisa de {} L de tinta'.format(tinta))

