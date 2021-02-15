'''62-melhore o desafio 61 perguntando para o usuario se ele quer mostrar mais alguns termos. o programa encerra quanto ele disserr que quer mostrar 0 termos. '''

n=int(input('digite um numero: '))
pa=int(input('digite pa: '))
termo=n
contador=1
total=0
mais=10
while mais!=0:
    total=total+mais
    while contador<=total:        
        print('{}'.format(termo), end='-')
        termo+=pa
        contador+=1
    print('PAUSA')
    mais=int(input('quantos termos voce quer mostrar ? ')) 
print('FIM')

                       #FIM//A\\