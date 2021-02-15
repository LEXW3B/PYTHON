'''64-CRIE UM PROGRAMA QUE LEIA VARIOS NUMEROS INTEIROS PELO TECLADO.O PROGRAMA SO VAI PARAR QUANDO O USUARIO DIGITAR O VALOR 999, QUE E A CONDIÇÃO DE PARADA. NO FINAL, MOSTRE QUANTOS NUMEROS FORAM DIGITADOS E QUAL FOI A SOMA ENTRE ELES(DESCONSIDERANDO O FLAG).FLAG E O 999 '''   

n=cont=soma=0
n=int(input('digite numero: '))
while n!=999:
    soma+=n
    cont+=1
    n=int(input('digite numero: '))
print('voce digitou {} numeros e a soma entre eles foi {}...FIM'.format(cont, soma))

                         #FIM//A\\