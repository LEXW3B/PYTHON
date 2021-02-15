#56-desenvolva um programa que leia o nome, idade e o sexo de 4 pessoas. no final do program,mostre:
#a media de idade do grupo
#qual e o nome do homem mais velho
#quantas mulheres tem menos de 20 anos
somaidade = 0
mediaidade=0
maioridadehome=0
nomevelho=''
totmulher20=0
for p in range(1, 5):
    print('{}ª pessoa:'.format(p))
    nome = str(input('NOME: ')).strip()
    idade = int(input('IDADE: '))
    sexo = str(input('SEXO [M/F] : ')).strip
    somaidade = somaidade+idade
    if p==1 and sexo in 'Mm':
        maioridadehome=idade
        nomevelho=nome
    if sexo in 'Mm' and idade > maioridadehome:
        maioridadehome=idade
        nomevelho=nome
    if sexo in 'Ff' and idade < 20:
        totmulher20+= 1
mediaidade = somaidade/4
print('a media da idade do grupo e de {} anos.'.format(mediaidade))
print('o homem mais velho tem {} anos e se chama {}.'.format(maioridadehome, nomevelho ))
print('ao todo sao {} mulheres com menos de 20 anos. '.format(totmulher20))

                              #FIM//A\\