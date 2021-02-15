'''66-crie um programa que leia varios numeros inteiros pelo teclado.o programa so vai parar quando o usuario digitar 999, que e a condicao de parada. no final, mostre quantos numeros foram digitados e qual foi a soma entre eles.desconsiderando o flag.   '''

s=n=contador=0
while True:
    n=int(input('999 para o programa: '))
    if n==999:
        break
    s+=n
    contador+=1
print(f'voce digitou {contador} numeros e a soma dos numeros foi {s}. ')

                         #FIM//A\\