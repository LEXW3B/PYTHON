#escreva um programa que leia a velocidade de um carro. se ele ultrapassar a velocidade de 80km/h,mostre uma menssagem dizendo que ele foi multado. a multa vai custar R$ 7,00 por cada km acima do limite.
vel = float(input('digite a velocidade:  '))
if vel > 80:
    print('voce ultrapassou {}km/h e foi multado.'.format(vel))
    multa = (vel - 80) * 7
    print('por cada km acima do limite sera cobrado ao todo R$ {:.2f}'.format(multa))
print('tenha um bom dia. dirija com cuidado.')
    
                         #fim//A\\