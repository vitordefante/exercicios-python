# programa que lê numeros inteiros  no final mostra quantos foram inseridos e sua soma total se o usuario botar 999
cont = 1
soma = 0
while True:
    num = int(input('Digite um número (999 pra parar): '))
    if num == 999:
        break
    cont += 1
    soma += num
print(f'\nForam digitados {cont} números e a soma entre eles é {soma}')
