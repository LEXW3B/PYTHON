#57-faça um programa que leia o sexo de uma pessoa,mas so aceite os valores M ou F.caso esteja errado, peça a digitação novamente ate ter um valor correto.

sexo = str(input('SEXO [M/F]: ')).strip().upper()[0]
while sexo not in 'MF':
    sexo = str(input('informação invalida.  informe sexo: ')).strip().upper()[0]
print('o sexo informado é {}. registrado com sucesso.'.format(sexo))


                        #FIM//A\\