'''59-crie um programa que leia dois valores e mostre um menu na tela:

#[1]somar
#[2]multiplicar
#[3]maior
#[4]novos numeros
#[5]sair do programa
# 
# seu programa devera realizar a operação solicitada em cada caso.'''



from time import sleep
v1=int(input('digite 1º valor: '))
v2=int(input('digite 2º valor: '))
operacao=0
while operacao!=5:
    print('qual operacao voce quer fazer com esses valores.')
    print('''
    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos numeros
    [ 5 ] sair do programa
    ''')
    operacao=int(input('digite o numero da operacao: '))
    if operacao == 1: 
        soma=v1+v2    
        print(' {} + {} = {}'.format(v1, v2, soma))
    elif operacao == 2:
        mult=v1*v2
        print(' {} x {} = {}'.format(v1, v2, mult))    
    elif operacao == 3:
        if v1>v2:
            maior=v1
        else:
            maior=v2
        print('entre {} é {} o maior valor é {}.'.format(v1, v2, maior))
    elif operacao == 4:
        v1=int(input('digite 1º numero: '))
        v2=int(input('digite 2º numero: '))
    elif operacao == 5:
        print('finalizando...')
    else:
        print('opcao invalida. tente novamente')
    print('=-='*10)
    sleep(2)
print('FIM DO PROGRAMA! VOLTE SEMPRE!')    

                           #FIM//A\\