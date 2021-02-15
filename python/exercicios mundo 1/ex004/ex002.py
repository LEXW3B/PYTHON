# Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.
import math
num =float(input('digite um valor: '))
print('o valor digitado foi {} e a porcao inteira e {}'.format(num, math.trunc(num)))