# programa que mostra se o numero inserido pelo usuário é par ou ímpar
num = int(input('Insira um número inteiro: ')) % 2
if num == 1:
    print('\nO número inserido é ímpar!')
else:
    print('\nO número inserido é par!')
