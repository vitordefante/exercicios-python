def leiadin(txt):

    dinheiro = input(f'\033[1m{txt}\033[m').strip().replace(' ', '')

    while dinheiro.isalpha() or dinheiro == '':
        print('\033[1;31mErro! Tente novamente apenas com números inteiros ou flutuantes.\033[m')
        dinheiro = input(f'{txt}').strip().replace(' ', '')

    dinheiro = dinheiro.replace(',', '.')
    dinheiro = float(dinheiro)
    return dinheiro

# a funçao pega uma string com números, tendo ou nao ponto ou vírgula, trata ela para a moeda real e depois retorna
#  em um número float