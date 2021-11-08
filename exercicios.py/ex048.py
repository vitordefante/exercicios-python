# programa que calcula a soma de numeros impares primos entre 1 e 500
soma = 0
for n in range(1, 501, 2):
    if n % 3 == 0:
        soma = soma + n
print('\nA soma dos números impares multiplos de 3 entre 1 e 500 é : {}'.format(soma))
