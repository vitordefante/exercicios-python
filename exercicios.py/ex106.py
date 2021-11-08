# mini sistema que utiliza o interactive help do python. o usuario vai digitar o comando e o manual vai aparecer.
from time import sleep


def pyhelp():
    while True:
        print('\033[1;34mSistema de ajuda PyHelp!\033[m')
        f = input('\033[1mFunçao ou biblioteca > ').strip()
        if f == 'fim':
            break
        print(f'Acessando o manual do comando {f}...\033[m ')
        sleep(0.35)
        print(help(f))
        sleep(0.35)


pyhelp()
