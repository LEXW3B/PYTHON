#faça um programa que leia uma frase pelo teclado e mostre.(quantas vezes aparece a letra 'a'),(em que posição aparece a primeira vez),(em que posição ela aparece a ultima vez).
frase = str(input('digite uma frase: ')).upper().strip()
print('a letra A aparece {} vezes na frase'.format(frase.count('A')))
print('a primeira letra A apareceu na posição {}'.format(frase.find('A')+1))
print('a letra A apareceu pela ultima vez na posição {}'.format(frase.rfind('A')+1))

                             #FIM//A\\
