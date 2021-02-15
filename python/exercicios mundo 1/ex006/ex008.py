#faça um programa que leia tres numeros e mostre qual e o maior e o menor.
a = int(input('primeiro valor: '))
b = int(input('segundo valor: '))
c = int(input('terceiro valor: '))
#verificando quem e o menor
menor = a
if b < a and b < c:
    menor = b
if c < a and  c < b:
    menor = c
#verificando que em o maior
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print('o menor valor digitado foi {}.'.format(menor))
print('o maior valor digitado foi {}.'.format(maior))

                                  #FIM//A\\