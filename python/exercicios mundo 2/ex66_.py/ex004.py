'''69-crie um programa que leia a idade e o sexo de varias pessoas.a cada pessoa cadastrada, o programa devera perguntar se o usuario quer ou nao continuar.no final mostre:
A- quantas pessoas tem mais de 18 anos.
B- quantos homensforam cadastrados.
C- quantas mulheres tem menos de 20 anos.    '''

tot18=toth=totm20=0
contador=sexo=0
while True:    
    idade=int(input('qual a idade: ')) 
    if idade>=18:
        tot18+=1
    if sexo =='M':
        toth+=1
    if sexo =='F'and idade<20:
        totm20+=1
    sexo=' '
    while sexo not in 'MF':  
        sexo=str(input('qual o sexo[M/F]: ')).upper().strip()[0]
    continua=' '
    while continua not in 'SN':
        continua=str(input('deseja continuar [S/N]: ')).upper().strip()[0]
    if continua=='N':
        break 
print(f'temos {tot18} pessoas com mais de 18 anos. ')
print(f'ao todo temos {toth} homens cadastrados')
print(f'e temos {totm20} mulheres com menos de 20 anos')
       
                     #FIM//A\\