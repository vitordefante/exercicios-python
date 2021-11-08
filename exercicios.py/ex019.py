import random
print('Sorteio para apagar o quadro')
print(' ')
print('Abaixo, escreva o nome dos quatro alunos para gerar um aletório entre eles')
print(' ')
aluno1 = input('Insira o nome do primeiro aluno: ')
aluno2 = input('Insira o nome do segundo aluno: ')
aluno3 = input('Insira o nome do terceiro aluno: ')
aluno4 = input('Insira o nome do quarto aluno: ')
aleatorio = aluno1, aluno2, aluno3, aluno4
aleatorio1 = (random.choice(aleatorio))
print(' ')
print('{} ganhou o sorteio para apagar o quadro.'.format(aleatorio1))
