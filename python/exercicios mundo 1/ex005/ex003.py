#crie um programa que leia o nome completo de uma pessoa.(o nome com todas as letras maiusculas),(o nome com todas minusculas),(quantas letras ao todo, sem considerar espaços),(quantas letras tem o primeiro nome).

nome = str(input('Digite seu nome completo: ')).strip()
print('analizando seu nome...')
print('seu nome em maiusculas é {}'.format(nome.upper()))
print('seu nome em minusculas é {}'.format(nome.lower()))
print('seu nome tem ao todo {}'.format(len(nome)-nome.count(' ')))
print('seu primeiro nome tem {} letrs'.format(nome.find(' ')))
                                  
                                  #FIM//A\\