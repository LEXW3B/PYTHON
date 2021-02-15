#43-desenvolva uma logica que leia o peso a altura de uma pessoa, calcule seu imc e mostre seu estatus, de acordo com a tabela abaixo:
#- abaixo de 18.5:abaixxo do peso
#- entre 18.5 e 25:peso ideal
#- 25 ate 30:sobrepeso
#- 30 ate 40:obesidade
#- acima de 40:obesidade morbida

peso = float(input('digite seu peso: '))
altura = float(input('digite sua altura: '))
imc = peso / (altura ** 2)
print('o imc dessa pessoa e de {:.1f}'.format(imc))
if imc < 18.5:
    print('voce esta abaixo do peso normal')
elif 18.5 <= imc < 25:
    print('parabens voce esta na faixa de peso')
elif 25 <= imc < 30:
    print('voce esta em sobrepeso')
elif 30 <= imc < 40:
    print('voce esta em obesidade, cuidado')
elif imc >= 40:
    print('voce esta em obesidade morbida, cuidado')

                               #FIM//A\\