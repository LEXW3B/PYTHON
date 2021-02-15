#37-escreva um programa que leia um numero inteiro qualquer e peça para o usuario escolher qual sera a base de conversão: decimal para
#1 - para binario
#2 - para octal
#3 - para hexadecimal
print('====================')
print('BASES DE CONVERSÃO')
print('--------------------')
print('1 - Para binário')
print('2 - Para octal')
print('3 - Para hexadecimal')
print('====================')
n1 = int(input('Escreva um número: '))
n2 = int(input('Escolha a base de conversão: '))
#=====================================================
if   n2 == 1:
    print('O resultado em binário é {}'.format(bin(n1)[2:]))#dentro do colchete esta fatiando tirando os dois primeiros numeros do resultado
elif n2 == 2:
    print('O resultado em octal é {}'.format(oct(n1)[2:]))#dentro do colchete esta fatiando tirando os dois primeiros numeros do resultado
elif n2 == 3:
    print('O resultado em hexadecimal é {}'.format(hex(n1)[2:]))#dentro do colchete esta fatiando tirando os dois primeiros numeros do resultado

                                #FIM//A\\