#escreva um programa que pergunte o salario de um funcionario e calcule o valor do seu aumento. para salarios superiores a 1.250,00, calcule o aumento em 10%. para os inferiores ou iguais o aumento e de 15%.
salario = float(input('quanto e seu salario: R$ '))

if salario > 1.250:
    novo = salario + (salario * 10 / 100)
    print('seu salario teve aumento, e ficou de {}.'.format(novo))
else:
    novo = salario + (salario * 15 / 100)
    print('seu salario teve almento, e ficou de {}.'.format(novo))

                               #FIM//A\\