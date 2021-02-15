#ex035-desenvolva um programa que leia o cumprimento de tres retas e diga ao usuario se elas podem ou nao formar um triangulo.
r1 = float(input('digite um numero: '))
r2 = float(input('digite um numero: '))
r3 = float(input('digite um numero: '))
print('analizador de triangulos')
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('os segmentos acima podem formar triangulo!')
else:
    print('os sesgmento acima não podem formar triangulo!')

                             #FIM//A\\