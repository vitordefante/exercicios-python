# funçao que gera valores aleatorios e coloca dentro de uma lista, funçao que pega os valores pares e faz a soma

from random import randint
from time import sleep

lista = []


def sorteia(lst):
    print('\n\033[1mSorteando 7 valores da lista: ', end='')
    sleep(0.35)
    for i in range(0, 7):
        numero = randint(1, 20)
        lista.append(numero)
        print(f'{lista[i]} ', end='')
        sleep(0.35)


def somapar(lst):
    soma = 0
    for s in lista:
        if s % 2 == 0:
            soma += s

    print('\n\nSomando os valores \033[1;36mpares\033[m\033[1m  ', end='')
    sleep(0.35)
    for n in lista:
        if n % 2 == 0:
            print(f'{n} ', end='')
            sleep(0.35)

    print(f'temos \033[1;36m{soma}')


sorteia(lista)
somapar(lista)
