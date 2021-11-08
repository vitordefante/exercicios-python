# pedra papel tesoura xD
import random
jogador = input('Insira pedra, papel ou tesoura para desafiar a maquina: ').upper().strip()
pedra = 'PEDRA'
papel = 'PAPEL'
tesoura = 'TESOURA'
ppt = pedra, papel, tesoura
maquina = (random.choice(ppt))
if jogador in maquina:
    print('O jogo empatou! Você jogou {} e a máquina também!.'.format(jogador))
elif 'PAPEL' in jogador and 'TESOURA' in maquina:
    print('Você perdeu! Maquina jogou {} e você jogou {}.'.format(maquina, jogador))
elif 'PAPEL' in jogador and 'PEDRA' in maquina:
    print('Você ganhou! Você jogou {} e a maquina jogou {}.'.format(jogador, maquina))
elif 'PAPEL' in maquina and 'TESOURA' in jogador:
    print('Você ganhou! Você jogou {} e a máquina jogou {}.'.format(jogador, maquina))
elif 'PAPEL' in maquina and 'PEDRA' in jogador:
    print('Você perdeu! A maquina jogou {} e você jogou {}.'.format(maquina, jogador))
elif 'PEDRA' in jogador and 'TESOURA' in maquina:
    print('Você ganhou! Você jogou {} e a máquina jogou {}.'.format(jogador, maquina))
elif 'TESOURA' in jogador and 'PEDRA' in maquina:
    print('Você perdeu. A máqiuna jogou {} e você jogou {}'.format(maquina, jogador))
# podendo também adicinar cores quando conveniente
