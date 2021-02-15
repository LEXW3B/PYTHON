#58-melhore o jogo do desafio 28 onde o computador vai pensar em um numero entre 0 e 10. so que agora o jogador vai tentar adivinhar ate acertar, mostrando no final quantoss palpites foram necessarios para vencer.

from random import randint
cpu=randint(1, 10+1)
print('Oi, sou seu computador...Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue adivinhar qual foi o número que eu escolhi ? ')
acertou=False
palpite=0
while not acertou:
    palpite+=1
    jogador=int(input('qual o seu palpite ? '))
    if jogador==cpu:
        acertou=True
    else:
        if jogador < cpu:
            print('MAIS...tente novamente.')
        elif jogador > cpu:
            print('MENOS...tente novamente.')
print('ACERTOU COM {} PALPITES.'.format(palpite))

                       #FIM//A\\
