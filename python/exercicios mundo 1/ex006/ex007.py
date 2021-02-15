#faça um programa que leia um ano qualquer e mostre se ele e bissexto.
from datetime import date
ano = int(input('que ano quer analizar ? '))
if ano == 0:#esse comando pega a data da maquina que ta rodando o programa
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('o ano {} é bissexto '.format(ano))
else:
    print('o ano {} não é bissexto.'.format(ano))

                               #FIM//A\\