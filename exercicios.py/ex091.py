# joga 4 dados e depois ordena um ranking do numero maior para o menor
from random import randint
from time import sleep

jogadores = {'Jogador1': randint(1, 6),
             'Jogador2': randint(1, 6),
             'Jogador3': randint(1, 6),
             'Jogador4': randint(1, 6)}
ordem = []
cont = 0

print('\033[1;36mValores sorteados:\033[m')
for jogador in jogadores:
    print('O {} tirou {}'.format(jogador, jogadores[jogador]))
    ordem.append(jogadores[jogador])
    sleep(0.6)

ordem.sort(reverse=True)
print('\n\033[1;34mRanking da partida:\033[m')

while cont < len(ordem):
    for x, y in jogadores.items():
        if cont == len(ordem):
            print('\033[1;31m\nJogo finalizado...\033[m')
            sleep(0.6)
            break
        if y == ordem[cont]:
            print('{}° lugar: {} com {}'.format(cont + 1, x, y))
            cont += 1
            sleep(0.6)


# a logica de funcionamento do sistema de ranking consiste em iterar sobre a ordem[cont] revertida enquanto cont for
#  menor que o numero de itens na ordem. se o y (valor do dado) for igual ao item na ordem, é imprimido o jogador e
#   o valor do item, como também sua classificaçao no ranking (1, 2, 3...) via o count + 1
