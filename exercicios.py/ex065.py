# programa que le varios numeros inteiros e no final motras a média, o maior e o menor numero
numeros = []
contador = 0
div = 0
while contador == 0:
    div = div + 1
    numero = int(input('Insira um número inteiro: '))
    numeros.append(numero)
    continuar = input('Deseja digitar mais algum valor? (S/N): ').strip().upper()
    if continuar != 'S' and continuar != 'N':
        print('Opçao inválida, tente novamente')
    elif continuar == 'S':
        continue
    elif continuar == 'N':
        break
soma = sum(numeros)
if max(numeros) == min(numeros):
    print('\nOs números tem o mesmo valor')
else:
    print(('\nO \033[1;35mmaior\033[m número lido é \033[1;35m{}\033[m e o \033[1;31mmenor\033[m é \033[1;31m{}\033[m'
           .format(max(numeros), min(numeros))))
print('\nA \033[1;34mmédia\033[m de todos os numeros inseridos é \033[1;34m{}\033[m'.format(soma / div))
