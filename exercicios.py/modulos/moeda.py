def metade(n, reais=False):
    if reais:
        return moeda(n / 2)
    return n / 2


def dobro(n, reais=False):
    if reais:
        return moeda(n * 2)
    return n * 2


def aumentar(n, porcento, reais=False):
    mai = porcento / 100 * n
    if reais:
        return moeda(n + mai)
    return n + mai


def diminuir(n, porcento, reais=False):
    dim = porcento / 100 * n
    if reais:
        return moeda(n - dim)
    return float(n - dim)


def moeda(n):
    """"param: O valor númerico pertencente a uma variável ou no parametro da chamada de funçao.
        return: Retorna o valor / parametro inserido acompanhado da moeda reais."""
    return '\033[1;32mR$\033[m{:.2f}'.format(n)


def resumo(n, dim=0, aum=0):
    print('\n\033[1;32m         Resumo do valor\033[m')
    print('\n\033[1mPreco analisado:        {}'.format(moeda(n)))
    print('Dobro do preço          {}'.format(dobro(n, True)))
    print('Metade do preço         {}'.format(metade(n, True)))
    if aum > 0:
        print('{}% de aumento:         {}'.format(aum, aumentar(n, aum, True)))
    if dim > 0:
        print('{}% de reduçao:         {}'.format(dim, diminuir(n, dim, True)))
