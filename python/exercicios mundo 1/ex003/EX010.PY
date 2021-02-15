#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
s = float(input('seu salario e R$ '))
reajust = s + (s * 15 / 100)
print('seu salario com o aumento de 15% fica R$ {}'.format(reajust))
    