'''61-refaça o desafio 51, lendo o primeiro termo e a razao de uma pa, MOSTRANDO OS 10 PRIMEIROS TERMOS DA PROGRESSÃO usando a estreutura while. '''

n=int(input('digite um numero: '))
pa=int(input('digite pa: '))
termo=n
contador=1
while contador<=10:
    print('{}'.format(termo), end='-')
    termo+=pa
    contador+=1
print('FIM')    

                           #FIM//A\\