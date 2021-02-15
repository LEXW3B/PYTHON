#crie um programa que leia um numero inteiro qualquer e mostre na tela se ele e par ou impar.
num = int(input('par ou impar ? '))
resultado = num % 2
if resultado == 0:
    print('o numero {} é par.'.format(num))
else:
    print('o numero {} é impar.'.format(num))
    
                            #FIM//A\\