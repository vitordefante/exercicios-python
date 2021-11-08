frase = input('Digite a seguir uma frase para saber se essa frase é ou nao é um palíndromo: ')\
    .replace(' ', '').strip().upper()
for polindromo in frase:
    if frase[::-1] in frase:
        print('\n\033[1;34mA frase é um palíndromo.')
        break
    else:
        print('\n\033[1;31mA frase inserida nao é um palíndromo.')
        break
