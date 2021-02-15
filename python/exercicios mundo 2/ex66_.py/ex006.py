'''71-crie um programa  que simule o funcionamento de um caixa eletronico.no inicio,pergunte ao usuario o valor que sera sacado(numero inteiro) e o programa vai informar quantas cedulas de cada valor seram entregues.
obs:.considere que o caixa possui cedulas de 50, 20, 10 e 1 real.  '''
print('='*30)
print('{:^30}'.format('BANCO CEV'))
print('='*30)
valor=int(input('O valor a ser sacado é ? '))
total=valor
ced=50
totced=0
while True:    
    if total>=ced:
        total-=ced
        totced+=1
    else:  
        if totced>0:
            print(f'total de {totced} cedulas de R$ {ced}')           
        if ced==50:
            ced=20    

        elif ced==20:
            ced=10
            
        elif ced==10:
            ced=1
        totced=0
        if total==0:
            break 
                          
print('='*30)        
print('volte sempre ao BANCO CEV! tenha um bom dia!')

                        #FIM//A\\