#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.
from math import hypot
co = float(input('comprimento do cateto opsto: '))
ca = float(input('comprimento do cateto adjacente: '))
hi = hypot(co, ca)
print('a hipotenusa vai medir {:.2f}'.format(hi))

