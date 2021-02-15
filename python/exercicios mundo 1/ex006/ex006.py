#desenvolva um programa que pergunte a distancia de uma viagem em km. calcule o preço da passagem, cobrando R$0,50 por km para viagens de ate 200km. e R$0,45 para viagens mais longas.
dis = float(input('qual a distancia da sua viagem ? '))
print('sua distancia percorrida e de {} km.'.format(dis))
if dis <= 200:
    preço = dis * 0.50
else:
    preço = dis * 0.45
print('O valor e de R$ {}'.format(preço))

                                      #FIM//A\\