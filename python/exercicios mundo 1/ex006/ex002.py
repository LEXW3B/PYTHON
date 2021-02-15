n1 = float(input('digite sua nota: '))
n2 = float(input('digite sua nota: '))
m = (n1 + n2) / 2
if m >=6.0:
    print('sua média foi {:.1f}.'.format(m))
    print('parabéns você PASSOU!!!')
else:
    print('sua média foi {}.'.format(m))
    print('REPROVADO! sem férias para você kkkkk')
