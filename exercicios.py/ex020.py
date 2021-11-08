from random import sample, shuffle
print('Insira os nomes dos quatro alunos e gere uma ordem de apresentaçao')
a1 = input('Primeiro aluno: ')
a2 = input('Segundo aluno: ')
a3 = input('Terceiro aluno: ')
a4 = input('Quarto aluno: ')
lista = [a1, a2, a3, a4]
print('A ordem abaixo representa respectivamente a ordem dos alunos a apresentar')
sample(lista, k=4)
print(lista)
