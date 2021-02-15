#48-faça um programa que calcule a soma entre todos os numero impares que sao multiplos de tres e que se encontram no intervalo de 1 ate 500.
soma = 0
contador = 0
for c in range (1, 500, 3 - 1):
    if c % 3 == 0:#SE C FOR DIVISIVEL POR 3 E O RESULTADO = A ZERO
        contador = contador + 1# TAMBEM PODE SER ...CONTADOR += 1...
        soma = soma + c#SOMA += C  SO PARA O CODIGO FICAR MAIS ENXUTO.
print('a soma de todos os {} valores solicitados é {}.'.format(contador, soma))        

           #FIM//A\\