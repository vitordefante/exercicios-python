# programa que le varios numeros e coloca em uma lista, depois faz uma lista com impar e outra com par e mostra as 3
numeros = []
pares = []
impares = []
while True:
    numero = int(input('\033[1mInsira um valor (-1 pra parar): '))
    if numero == -1:
        break
    numeros.append(numero)
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)
print('\nOs números \033[1;32minseridos\033[m\033[1m foram {}'.format(numeros))
print('Os números \033[1;34mpares\033[m\033[1m inseridos foram {}'.format(pares))
print('Os números \033[1;33mímpares\033[m\033[1m inseridos foram {}'.format(impares))
