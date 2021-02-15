#39-faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade.
# -se ele ainda vai se alistar ao serviço militar.
# -se e a hora de se alistar.
# -se ja passou do tempo do alistamento.
# seu programa tambem devera mostrar o tempo que falta ou que passou do prazo. 
ano = int(input('digite ano atual: '))
idade = int(input('digite ano de nascimento: '))
n1 = ano - idade
if n1 < 18:
    print('você só tem {} anos, ainda não pode se alistar no serviço militar.'.format(n1))
elif n1 == 18:
    print('Você tem {} anos. Está na hora de se alistar no serviço militar'.format(n1))
elif n1 > 18:
    print('você tem {} anos. Já passou da hora de se alistar no serviço militar.'.format(n1))

                             #FIM//A\\        