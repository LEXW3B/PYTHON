#LAÇOS DE REPETICAO
#49-REFAÇA O DESAFIO 009 , MOSTRANDO A TABUADA DE UM NUMERO QUE O USUARIO ESCOLHER, SO QUE AGORA UTILIZANDO UM LAÇO FOR.
print('')
print('=-=-=-=-=-=TABUADA=-=-=-=-=-=')
print('')
numero = int(input('digite um numero: '))
for cont in range (1, 11):
    print('{} x {:2} = {}'.format(numero, cont, numero*cont))

                    #FIM//A\\