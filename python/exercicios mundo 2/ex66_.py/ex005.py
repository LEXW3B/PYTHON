'''70-crie um programa que leia o nome e o preco de varios produtos. o programa devera perguntar se o usuario vai continuar.no final mostre:
A- qual e o total gasto na compra.
B- quantos produtos custam mais de 1000.
C- qual o nome do produto mais barato.   '''
cont=menor=total=totmil=0
barato=' '
while True:
    produto=str(input('qual o nome do produto: ')).upper().strip()
    preco=int(input('qual o preco do produto: ')) 
    cont+=1 
    total+=preco
    if preco>1000:
        totmil+=1
    if cont==1 or preco<menor:
        menor=preco
        barato=produto
    resp=' '
    while resp not in 'SN': 
        resp=str(input('vai continuar[S/N]: ')).upper().strip()[0]
    if resp!='S':
        break       
print('{:-^40}'.format('FIM DO PROGRAMA'))   
print(f'O total da sua compra foi de R$ {total:.2f} ')
print(f'{totmil} produtos custam mais de R$ 1000   ')
print(f'o nome do produto mais barato e {barato} que custou R$ {menor:.2f} ')
print('=-'*40)

                         #FIM//A\\