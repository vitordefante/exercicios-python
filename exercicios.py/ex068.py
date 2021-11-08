# jogo de par ou ímpar, o jogo será interrompido quando o usuário perder
from random import randint
# colors
bold = '\033[m'
red = '\033[1;31m'
green = '\033[1;32m'
yellow = '\033[1;33m'
blue = '\033[1;34m'
purple = '\033[1;35m'
neonblue = '\033[1;36m'

cont = 0  # contador
while True:  # looping infinito, encerrado apenas via break
    cont += 1
    maquina = randint(1, 10)
    imparpar = str(input('\n\033[1mVocê deseja par ou ímpar? [P/I]: ')).strip().upper()
    jogador = int(input('\033[1mDigite um número: '))
    soma = maquina + jogador
    if 'I' in imparpar and soma % 2 == 0:
        print('\nVocê jogou {} e o computador jogou {}. Total de {} e deu par! \nVocê perdeu!\nVocê sobreviveu {} '
              'rodadas! Encerrando o jogo...\n'
              .format(jogador, maquina, soma, cont - 1))
        break
    elif 'I' in imparpar and soma % 2 != 0:
        print('\nVocê jogou {} e o computador jogou {}. Total de {} e deu ímpar!\nVocê ganhou! Vamos jogar novamente...'
              .format(jogador, maquina, soma))
    elif 'P' in imparpar and soma % 2 == 0:
        print('\nVocê jogou {} e o computador jogou {}. Total de {} e deu par!\nVocê ganhou! Vamos jogar novamente...'
              .format(jogador, maquina, soma))
    elif 'P' in imparpar and soma % 2 != 0:
        print('\nVocê jogou {} e o computador jogou {}. Total de {} e deu ímpar! \nVocê perdeu!\nVocê sobreviveu {} '
              'rodadas! Encerrando o jogo...\n'.format(jogador, maquina, soma, cont - 1))
        break
#  a lógica do código varia se o jogador botou impar ou par, se ele botar par ou impar e o total nao satisfazer a condi
#   çao, a funçao break é aplicada e o aplicativo encera, se o par ou impar estiver de acordo com o total, o looping segue
