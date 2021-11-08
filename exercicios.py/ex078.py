# programa que lê 5 valores numéricos e guarda numa lista, no final, mostra o maior e o menor valor
numeros = []
maiores = []
for numero in range(0, 5):
    numeros.append(int(input('\033[1mInsira um valor para a Posiçao {}: '.format(numero))))
print('\nVocê digitou os valores {}'.format(numeros))
print('O maior valor digitado foi {} na posiçao: '.format(max(numeros)), end='')
for m in range(len(numeros)):
    if numeros[m] == max(numeros):
        print(f'{m:.<3}', end='')
print('\nO menor número digitado foi {} e se encocntra na posiçao '.format(min(numeros)), end='')
for i in range(len(numeros)):
    if numeros[i] == min(numeros):
        print(f'{i:.<3}', end='')
print('\n')