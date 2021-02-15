#escreva um programa que faça o computador pensar em um numero inteiro entre 0 e 5 e peça para o usuario tentar descobrir qual foi o numero escolhido pelo computador.
#o programa devera escrever na tela se o usuario venceu ou perdeu.
from random import randint
from time import sleep#faz o pc esperar alguns segundos
computador = randint (0, 5)#faz o pc pensar.
jogador =int(input('descubra o numero que o computador vai escolher de 0 a 5: '))#jogador
print('PROCESSANDO...')
sleep(3)#faz o pc esperar alguns segundos
if jogador == computador:
    print('parabens você adivinho o meu numero')
else :
    print('você errou. tente de novo.')

                              #FIM//A\\
