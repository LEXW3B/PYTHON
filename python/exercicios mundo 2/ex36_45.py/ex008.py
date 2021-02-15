#42-refaça o desafio dos triangulos, acrescentando o recurso de mostrar que tipo de triangulo sera formado:
#-equilatero:todos os lados iguais
#-isosceles:dois lados iguais
#-escaleno:todos os lados diferentes.
n1 = int(input('primeiro número: '))
n2 = int(input('segundo  número: '))
n3 = int(input('terceiro número: '))
print('analizador de triangulos')
if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n1 + n2:
    print('os segmentos acima podem formar triangulo!')
    if n1==n2==n3:
        print('EQUILATTERO')
    elif n1!=n2!=n3!=n1:
        print('ESCALENO')
    else:
        print('ESOSCELES')  
else:
    print('os segmento acima não podem formar triangulo!')

                         #FIM//A\\
