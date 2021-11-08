# exercicio que insere os números em uma tabela e mostra a tabela
tabela = [[], [], []]
pares = []
coluna3 = 0
x = 0
y = 0

for c in range(0, 9):
    n = int(input('Digite um valor para [{}, {}]: '.format(x, y)))

    tabela[x].append(n)
    if n % 2 == 0:
        pares.append(n)

    y += 1
    if y == 3:
        coluna3 += n
        y = 0
        x += 1
    if x == 3:
        x = 0


print('\033[1m')
for t in range(0, 9):
    print('[ {:^5} ]'.format(tabela[x][y]), end='')

    y += 1
    if y == 3:
        print('')
        y = 0
        x += 1

print('\nA soma dos valores pares é \033[1;32m{}\033[m\033[1m'.format(sum(pares)))
print('A soma dos valores da terceira coluna é \033[1;36m{}\033[m\033[1m'.format(coluna3))
print('O maior valor da segunda linha é \033[1;33m{}\033[m\033[1m'.format(max(tabela[1])))
