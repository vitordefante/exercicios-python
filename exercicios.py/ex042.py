# programa que le retas e informa se elas formam triangulo equilatero, isósceles ou escaleno
a = float(input('Insira o comprimento da primeira reta: '))
b = float(input('Insira o comprimento da segunda reta: '))
c = float(input('Insira o comprimento da terceira: '))
if a < b + c and b < a + c and c < a + b:
    print('\n\033[1;34mA soma das retas forma um triângulo.\033[m')
    if a == b == c:
        print('O triângulo é \033[1;32mequilátero.')
    elif a == b or a == c or b == c:
        print('O triangulo formado é \033[1;35misósceles.')
    elif a != b != c:
        print('Os triangulo formado é \033[1;36mescaleno.')
else:
    print('\n\033[1;31mA soma das retas nao forma um triângulo.')
