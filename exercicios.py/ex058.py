# nova versao do exercicio 28, onde o usuário precisa adivinhar o número entre 1 - 10 que a máquina pensou
# agora o jogador adivinha até acertar, e depois é mostrado quantos palpites foram necessários
from random import randint
tentativas = 0
maquina = randint(0, 10)
jogador = int(input('\033[1;36mInsira o número de 1 a 10 que foi gerado pela máquina:\033[m '))
if jogador == maquina:
    print('\n\033[1;32mParabéns, você ganhou de primeira!\033[1;35m A máquina jogou {} e você jogou {} também!'
          .format(maquina, jogador))
while jogador != maquina:
    jogador = int(input('\033[1;31mVocê errou!\033[1;33m Tente novamente: '))
    tentativas = tentativas + 1
    if jogador == maquina:
        print('\033[1;34mParabéns, você acertou! A máquina jogou {} e você jogou {} também! Foram necessárias {}'
              ' tentativas.'.format(jogador, maquina, tentativas + 1))
        break
# foi utilizada a funçao break para quebrar o loop após o print de vitória quando o jogador inserir o mesmo
# < numero que a maquina
