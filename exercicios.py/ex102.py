from math import factorial


def fatorial(n, show=False):
    """"A funçao calcula o fatorial de um número e mostra o cálculo.
        param n: número a ser calculado o fatorial
        show = (False/True) Indicar se é pra mostrar o cálculo inteiro
        return: Sem retorno"""
    fac = factorial(n)
    if not show:
        x = factorial(n)
        print(fac)
    if show:
        while n > 0:
            print(f'{n} ', end='')
            print('x ' if n > 1 else '= ', end='')
            n -= 1
        print(fac)


fatorial(5, show=True)
help(fatorial)

