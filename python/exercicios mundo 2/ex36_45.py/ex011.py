#45-crie um programa que faça o computador jogar jokenpo com voce.
print('=====JOKENPO=====')
print('')
from random import randint
from time import sleep
itens = ('pedra','papel','tesoura')
computador = randint(0, 2)
print('''FAÇA SUA ESCOLHA

[ 0 ] pedra
[ 1 ] papel
[ 2 ] tesoura
''')
jogador = int(input('Qual a sua jogada ? '))

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')
sleep(1)

print('computador jogou {}.'.format(itens[computador]))
print('jogador jogou {}.'.format(itens[jogador]))

if computador == 0: #computador jogou pedra
    if jogador == 0:
        print('EMPATE')

    elif jogador == 1:
        print('JOGADOR VENCE')

    elif jogador == 2:
        print('COMPUTADOR VENCE')

    else:
        print('jogada invalida')
elif computador == 1: #computador jogou papel
    if jogador == 0:
        print('COMPUTADOR VENCE') 

    elif jogador == 1:
        print('EMPATE')

    elif jogador == 2:
        print('JOGADOR VENCE')
    
    else:
        print('jogada invalida')
elif computador == 2: #computador jogou tesoura
    if jogador == 0:
        print('JOGADOR VENCE')

    elif jogador == 1:
        print('COMPUTADOR VENCE')

    elif jogador == 2:
        print('EMPATE')

    else:
        print('jogada invalida')

                          #FIM//A\\