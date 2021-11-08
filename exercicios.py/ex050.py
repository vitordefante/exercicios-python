# programa que lê seis números inteiros e mostra apenas a soma entre os pares
soma = 0
print('')  # blank line
for x in range(0, 6):
    numero = int(input('Insira o {}° valor: '.format(x + 1)))
    if numero % 2 == 0:
        soma += numero
print('A soma entre os números PARES inseridos é de \033[1;34m{}'.format(soma))
