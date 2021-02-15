#50-desenvolva um programa que leia 6 numeros inteiros e mostre a soma apenas da queles que forem pares.se o valor digitado for impar, desconsidere-o.

soma=0         # criacao de um somatorio
contador=0     # criacao de um contador
for c in range (1, 7):
    num = int(input('digite o {}° valor:  '.format(c)))
    if num % 2 == 0:  # se o numero for divisivel por 2 e igual a zero. isso e para pegar somente os numeros pares.
        soma += num
        contador = contador + 1
    print('Você informou {} números PARES é a soma deles foi {}.'.format(contador, soma))

                     #FIM//A\\