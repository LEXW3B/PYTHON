#40-classico
#crie um programa que leia duas notas do aluno e calcule sua media, mostrando uma mensagem no final, de acordo com a media atingida.
#-media abaixo de 5.0: REPROVADO
#-media entre 5.0 e 6.9: RECUPERAÇÃO
#-media 7.0 ou superior: APROVADO

n1 = float(input('digite nota: '))
n2 = float(input('digite nota: '))
m = (n1 + n2) / 2
if 7 > m >= 5:
    print('você está de RECUPERAÇÃO. Sua média foi {}.'.format(m))
elif  m < 5:
    print('REPROVADO.Sua média foi {}.'.format(m))
else:
    print('parabéns você está APROVADO. Sua média foi {}.'.format(m))

                           #FIM//A\\