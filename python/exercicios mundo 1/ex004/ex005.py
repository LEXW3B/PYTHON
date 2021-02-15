#Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.

import random
n1 =str(input('primeiro aluno: '))
n2 =str(input('segundo aluno: '))
n3 =str(input('terceiro aluno: '))
n4 =str(input('quarto aluno: '))
list = [n1, n2, n3, n4]
escolhido = random.choice(list)
print('o aluno escolhido foi {}'.format(escolhido))
    