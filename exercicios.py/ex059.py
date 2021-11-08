# programa que lê dois valors e mostra um menu na tela, o menu contém 5 opçoes e deve funcionar até o usuario sair
# colors
from time import sleep
none = '\033[m'
blank = '\033[1;m'
blue = '\033[1;34m'
purple = '\033[1;35m'
lightblue = '\033[1;36m'
red = '\033[1;31m'
green = '\033[1;32m'
yellow = '\033[1;33m'
back = '\033[1;30;46m'

print('{}Insira dois valores a seguir para receber um menu de opçoes.\033[m\n'.format(blank))
n1 = float(input('Insira o primeiro valor: '))
n2 = float(input('Insira o segundo valor: '))
menu = 6
while menu != 5:
    menu = int(input(
        '\n{}O que deseja fazer com os números inseridos? ({:.2f} e {:.2f}){}\n{}[1] Somar\n{}[2] Multiplicar \n{}[3] Maior numero \n'
        '{}[4] Inserir números novamente \n{}[5] Sair do programa\n{}'.format(back, n1, n2, none, blue, purple, green, yellow,
                                                                              red, blank)))
    if menu == 1:
        print('{}O valor soma entre {:.2f} e {:.2f} é \033[1;32m{:.2f}\033[m\nRetornando ao menu...'.format(none, n1, n2, n1 + n2))
        sleep(2.8)
    elif menu == 2:
        print('A multiplicaçao entre {:.2f} e {:.2f} tem como resultado \033[1;32m{:.2f}\033[m\nRetornando ao menu...'.format(n1, n2, n1 * n2))
        sleep(2.8)
    elif menu == 3:
        if n1 == n2:
            print('Os números inseridos tem o mesmo valor.\nRetornando ao menu...')
        else:
            print('O maior número entre os dois inseridos é \033[1;32m{:.2f}\033[m\nRetornando ao menu...'.format(max(n1, n2)))
        sleep(2.8)
    elif menu == 4:
        print('Insira os números novamente...\n')
        sleep(0.7)
        n1 = float(input('Insira o primeiro valor: '))
        n2 = float(input('Insira o segundo valor: '))
    elif menu == 0 or menu > 5:
        print('{}Opçao inválida{}, tente novamente com os números indicados.\nRetornando ao menu...'.format(red, none))
        sleep(1.4)
print('\n{}Aplicativo encerrado.'.format(yellow))
