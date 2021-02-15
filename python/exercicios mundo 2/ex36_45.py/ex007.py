#41-a confederação nacional de natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
#ate 9 anos:mirin
#ate 14 anos:infantil
#ate 19 anos:junior
#ate 20 anos:senior
#acima:master 

from datetime import date
atual = date.today().year
nascimento = int(input('digite o ano de nascimento: '))
idade = atual - nascimento
id1 = 9 
id2 = 14
id3 = 19
id4 = 20
if idade <= 9:#ok
    print('Você tem {} anos, sua categoria é a {}.'.format(idade, 'mirin'))
elif idade <= 14:
    print('Você tem {} anos. Sua categoria é a {}.'.format(idade, 'infantil'))
elif idade <= 19:
    print('Você tem {} anos. Sua categoria é {}.'.format(idade, 'junior')) 
elif idade <= 20:
    print('voce tem {} anos. sua categoria e {}.'.format(idade, 'senior'))
else:
    print('você tem {} anos. sua categoria é {}.'.format(idade, 'master'))

                            #FIM//A\\
