# faça uma funçao contador
from time import sleep


def contador(I, F, P):
    if P == 0:
        P = 1
    if P < 0:
        P *= (-1)
    print(f'\033[1mContagem de {I} até {F} de {P} em {P}:\033[m')
    if I < F:
        F += 1
    if I > F:
        F -= 1
        P += -P + -P
    for n in range(I, F, P):
        print(f'{n} ', end='')
        sleep(0.45)
    print('\n')


contador(1, 10, 1)
contador(10, -1, -2)

print('\n\033[1;32mAgora é sua vez de personalizar a contagem!\033[m')
i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
print('')

contador(i, f, p)
print('')
