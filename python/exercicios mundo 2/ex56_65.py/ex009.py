'''65-CRIE UM PROGRAMA QUE LEIA VARIOS NUMEROS INTEIROS PELO TECLADO. NO FINAL DA EXECUÇÃO , MOSTRE A MEDIA ENTRE TODOS OS VALORES E QUAL FOI O MAIOR E O MENOR VALOR LIDO. O PROGRAMA DEVE PERGUNTAR AO USUARIO SE ELE QUER OU NÃO CONTINUAR A DIGITAR VALORES. '''


resposta='S'
soma=quantidade=media=maior=menor=0
while resposta in 'Ss':
    n=int(input('digite numero: '))
    soma+=n
    quantidade+=1
    if quantidade ==1:
        maior=menor=n
    else:
        if n>maior:
            maior=n
        if n<menor:
            menor=n
    resposta=str(input('quer continuar? [S/N] ')).upper().strip()[0]
media=soma/quantidade

print('voce digitou {} numeros e a media foi {}'.format(quantidade, media))
print('o maior numero foi {} e o menor numero foi {}'.format(maior, menor))

                             #FIM//A\\