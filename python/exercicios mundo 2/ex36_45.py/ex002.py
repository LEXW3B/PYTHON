#36-======PEDIDO DO CLIENTE================OLHE TUDO ITALO
#escreva um programa para aprovar o emprestimo bancario para a compra de uma casa. o programa vai perguntar o valor da casa, o salario do comprador e em quantos anos ele vai pagar.
#calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salario ou então o emprestimo sera negado.
 
n1 = float(input('Qual o valor da casa: R$ '))
n2 = float(input('Quanto você ganha: R$ '))
n3 = int(input('Quantos anos para pagar: '))
vn = n1 / (n3 * 12)          # vn formula pra saber quantos meses
vm = (n2 * 30) / 100         # vm e formula pra saber quanto pode gastar max.30%
prestacao = n1 / vn          # formula pro valor da prestação 
print('O valor da prestação será de R$ {:.2f}'.format(prestacao))
print('O valor que você pode gastar é até R$ {:.2F} '.format(vm))
if vm < prestacao:
    print('Emprestimo NEGADO.')
else:
    print('Meus parabéns, você foi APROVADO(A)')

                              #FIM//A\\
