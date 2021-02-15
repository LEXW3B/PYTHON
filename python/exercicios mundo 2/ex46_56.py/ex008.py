#52-faça um programa que leia um numero inteiro e diga se ele e ou nao um numero primo.

numero = int(input('digite um numero: '))
tot = 0
for c in range (1, numero + 1):
    if numero % c == 0:
        print('\033[33m',end='' )
        tot += 1
    else:
        print('\033[31m',end='')
    print('{}'.format(c),end='')
print('  o numero {} foi divisivel {} vezes.'.format(numero, tot))
if tot == 2:
    print('e por isso ele e PRIMO')
else:
    print('e por isso ele nao e PRIMO')

                         #FIM//A\\
