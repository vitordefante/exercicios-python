# programa que lê quatro valores, no final, mostra quantas vezes 9, primeiro 3 index, quais os números pares
valores = ([])
pares = ([])

for x in range(1, 5):
    n = int(input('Digite um valor: '))
    valores.append(n)
    if n % 2 == 0:
        pares.append(n)
nove = valores.count(9)
print('\n\033[1mO valor 9 apareceu {} vezes.'.format(nove))
if 3 not in valores:
    print('O número 3 nao foi digitado.')
else:
    print('O número 3 foi digitado na {}ª posiçao'.format(valores.index(3) + 1))
print('Os números pares inseridos foram: {}.'.format(pares))
