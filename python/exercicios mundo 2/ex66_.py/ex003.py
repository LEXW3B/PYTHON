'''68-faca um programa que joguem par ou impar com o computador. o jogo so sera interrompido quando o jogador perder, mostrando o total de vitorias consecutivas que ele conquistou no final do jogo   '''
from random import randint
v=0
while True:
    jogador=int(input('digite um valor: '))
    computador=randint(0, 10)
    total=jogador+computador
    tipo=' '
    while tipo not in 'PI':
        tipo=str(input('par ou impar ? [P/I] ')).upper().strip()[0]
    print(f'voce jogou {jogador} e o computador jogou {computador}.Total de {total} ')
    print('deu par'if total%2==0 else 'deu impar')
    if tipo=='P':
        if total%2==0:
            print('VOCE VENCEU!!!')
            v+=1
        else:
            print('VOCE PERDEU!!!')
            break
    elif tipo=='I':
        if total%2==1:
            print('VOCE VENCEU!!!')
            v+=1
        else:
            print('VOCE PERDEU!!!')
            break
    print('vamos jogar novamente...')
print(f'GAME OVER!!!voce venceu {v} vezes. ')                    

                       #FIM//A\\