# cria uma funçao max()
from time import sleep
def maior(lst):
    m = lst[0]
    for x in lst:
        if x > m:
            m = x
    for y in lst:
        print(f'\033[1m{y} ', end='')
        sleep(0.35)
    print(f'foram informados {len(lst)} valores ao todo.')
    print(f'O maior valor informado foi {m}.\n')


lista1 = [1, 4, 5, 7, 4, 3, 4, 6, 7, 4]
lista2 = [3, 5, 3, 4, 1, 2, 3, 7]
lista3 = [5, 4, 3, 2, ]
lista4 = [43, 45, 213, 123, 654, 776, 12476, 8653]
maior(lista1)
maior(lista2)
maior(lista3)
maior(lista4)