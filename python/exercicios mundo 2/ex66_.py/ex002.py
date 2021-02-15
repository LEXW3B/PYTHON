'''67-FACA UM PROGRAMA QUE MOSTRE A TABUADA DE VARIOS NUMEROS, UM DE CADA VEZ, PARA CADA VALOR DIGITADO PELO USUARIO.O PROGRAMA SERA INTERROMPIDO QUANDO O NUMERO SOLICITADO FOR NEGATIVO.   '''
cont=0   
while True: 
    n=int(input('digite um numero: '))
    if n<0:
        break
    print('-'*30)  
    for cont in range (1, 11):
        print(f'{n} x {cont:2} = {n*cont}')
    print('-'*30)
    cont+=1
    
print('programa de tabuada encerrado.')
print('FIM')

                   #FIM//A\\