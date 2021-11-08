# programa que lê varios números e no final mostra quantos foram digitados e a soma entre eles
inf = 0
cont = 0
numeros = []  # lista anexar os números e depois somar usando o sum()
while inf == 0:
    numero = int(input('\033[1;32mDigite um número inteiro ou \033[1;33m999\033[1;32m para sair:\033[m '))
    if numero == 999:
        break
    numeros.append(numero)
    cont = cont + 1
print('\n\033[1mForam digitados um total de \033[1;35m{}\033[m números.'.format(cont))  # contagem de quantos numeros
print('\033[1mA soma de todos os números inserdos é \033[1;36m{}\033[m. '.format(sum(numeros)))  # sum() para soma da lista
