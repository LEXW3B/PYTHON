#54-crie um programa que leia o ano de nascimento de sete pessoas. no final, mostre quantas pessoas ainda nao atingiram a maioridade e quantas ja sao maiores.

from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for buceta in range (1, 8):
    nascimento = int(input('em que ano a {}ª pessoa nasceu ? '.format(buceta)))
    idade = atual - nascimento
    if idade >= 21:
        totmaior+=1
    else:
        totmenor+=1
print('ao todo tivemos {} pessoas de maior e {} pessoas de menor.'.format(totmaior, totmenor))

                    #FIM//A\\