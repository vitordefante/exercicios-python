#  programa que lê um número inteiro e informa se é ou nao é um numero primo
n = int(input('\nDigite um número inteiro para saber se é primo ou nao: '))
for x in range(2, n):
    if n % x == 0:
        print('\nO número inserido \033[1;31mnao é primo\033[m, pois {}/{} = {}'.format(n, x, n/x))
        break

    else:
        print('\n\033[1;32mO número inserido é primo')
        break

#  TODOS numeros primos sao maiores que um, NENHUM número primo é divisivel por outro número além de 1 ou ele mesmo

#  for x in range(2, n):
#     if n % x == 0:
#  o código baseia-se principalmente nas linhas acima, pois o loop divide o numero inserido por todos
#    os números de 2 até um número antes do inserido, se detectar alguma divisao inteira sem resto, o programa
#        informa por qual número o número inserido foi divido, mostra o resultado e informa que nao é primo.
#  O programa utilizou funçoes das quais nao foram aprendidas na aula, portanto analisar a correçao
#         e ver qual a outra possibilidade
#  todo número é dividido por 1 ou por ele mesmo
