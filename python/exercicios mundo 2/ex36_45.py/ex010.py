#44-elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
#-a vista dinheiro/cheque:10% de desconto
#-a vista no cartão:5% de desconto
#-em ate 2 vezes no cartão:preço normal
#-3x ou mais no cartão:20% de juros

print('{:=^40}'.format(' LOJAS FACADA '))
print('')
print('')
preco = float(input('digite o valor R$ '))#valor do produto
print('')
print('''FORMAS DE PAGAMENTO
[ 1 ] a vista dinheiro/cheque
[ 2 ] a vista cartao
[ 3 ] 2x no cartao
[ 4 ] 3x ou mais no cartao
''')
print('')
opcao = int(input('qual a forma de pagamento ? '))#como vai ser pago
if opcao == 1:
    total = preco - (preco * 10 /100)    
elif opcao == 2:
    total = preco - (preco * 5 / 100)
elif opcao ==3:
    total = preco
    parcela = total / 2
    print('sua compra sera parcelada em 2x de R$ {:.2f} SEM JUROS'.format(parcela))
elif opcao == 4:
    total = preco + (preco * 20 / 100)
    totalparcela = int(input('quantas parcela ? '))
    parcela = total / totalparcela
    print('sua compra de {}x vai custar R$ {:.2F} COM JUROS.'.format(totalparcela, parcela))
else:
    total = preco
    print('OPCAO INVALIDA de pagamento. tente novamente!')
print('sua compra e de R$ {:.2f} vai custa R$ {:.2f} no final.'.format(preco, total))

                             #FIM//A\\