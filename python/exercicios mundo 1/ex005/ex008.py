#faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o ultimo nome separadamente.ex...(ana maria de souza.....primeiro=ana.....ultimo=souza).
n = str(input('digite seu nome completo: ')).strip()
nome = n.split()
print('seu primeiro no é {}'.format(nome[0]))
print('seu ultimo nome é {}'.format(nome[len(nome)-1]))

                             #FIM//A\\
