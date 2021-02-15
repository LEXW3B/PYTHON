#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
import math
angulo = float(input('digite o angulo que voce deseja: '))
seno = math.sin(math.radians(angulo))
print('o angulo de {} tem o SENO de {:.2f}'.format(angulo, seno))
cosseno = math.cos(math.radians(angulo))
print('o angulo de {} tem o COSSENO de {:.2f}'.format(angulo, cosseno))
tangente = math.tan(math.radians(angulo))
print('o angulo de {} tem a TANGENTE de {:.2f}'.format(angulo, tangente))

