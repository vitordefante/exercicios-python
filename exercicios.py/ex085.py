# o usuario digita 7 valores em uma lista, que separa entre pares e ímpares, depois mostra eles em ordem crescente
numeros = [[], []]
for x in range(0, 7):
    numero = int(input('Insira um valor: '))
    if numero % 2 == 0:
        numeros[0].append(numero)
    else:
        numeros[1].append(numero)
print('\nOs valores pares digitados foram: {}'.format(sorted(numeros[0])))
print('Os valores ímpares digitados foram: {}'.format(sorted(numeros[1])))

#  predefine duas sublistas dentro de uma só lista, numeros[0] armazena os números pares e numeros[1] os ímpares.
