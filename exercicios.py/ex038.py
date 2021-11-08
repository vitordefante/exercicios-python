# programa que lê dois numero que faça a comparaçao entre eles de maior, menor ou igual
n1 = int(input('Insira um número inteiro aqui: '))
n2 = int(input('Insira o segundo número inteiro aqui: '))
if n1 > n2:
    print('\n\033[1;34mO primeiro número é maior.')
elif n2 > n1:
    print('\n\033[1;35mO segundo número é maior.')
else:
    print('\n\033[1;33mOs dois números possuem o mesmo valor.')
