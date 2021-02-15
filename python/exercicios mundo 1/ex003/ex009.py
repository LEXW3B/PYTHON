#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
p = float(input('o preço é: R$ '))
des = p - (p * 5 / 100)
print('o produto com seu desconto ficara por R$ {}'.format(des))
    