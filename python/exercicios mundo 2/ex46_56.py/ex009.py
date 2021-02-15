#53crie um programa que leia uma frase qualquer e diga se ela e um palindromo, desconsiderando os espaços. 

frase = str(input('digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto)-1, -1, -1):
    inverso+=junto [letra]
if inverso == junto:
    print('temos um palindromo')
else:
    print('a frase digitada nao e um palindromo')

                   #FIM//A\\