'''60-faça um programa que leia um numero qualquer na tela e mostre o seu fatorial.
EX:. 
5 = 5x4x3x2x1=120 '''

n=int(input('digite um nnumero a ser fatorado: '))
c=n
f=1
print('calculando {}! = '.format(n), end='')
while c>0:
    print('{}'.format(c),end='')
    print(' x ' if c > 1 else ' = ', end='')
    f*=c
    c-=1
print('{}'.format(f))

                    #FIM//A\\

'''from math import factorial
n=int(input('digite um nomero para ser fatorado: '))
f=factorial(n)
print('o fatorial de {} é {}.'.format(n, f))'''
