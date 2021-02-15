#51-desenvolva um programa que leia o primeiro termo e a razao de uma pa.no final, mostre os 10 primeiros termos dessa progressao.
num = int(input('digite um numero: '))
r   = int(input('digite razao: '))
decimo=num+(11-1)*r
for c in range (num, decimo, r):
    print(c, end='→')#Criar uma seta apontando para cima e para baixo , digitando " Alt + 23". Enter " Alt + 26" por uma seta horizontal "direita" ou " Alt + 27 " para fazer uma seta "esquerda" . Faça uma seta apontando para a direita ea esquerda , digitando " Alt + 29 " .
print('ACABOU')

                      #FIM//A\\