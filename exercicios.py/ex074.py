# programa que gera cinco núnmeros aleatórios e bota eles dentro de uma tupla
from random import randint

randoms = ([])
for random in range(0, 5):
    rand = randint(1, 20)
    randoms.append(rand)
maior = max(randoms)
menor = min(randoms)
print('\033[1;35mOs números gerados pela máquina foram: {}'.format(randoms))
print('\033[1;34mO maior número gerado pela máquina foi {}\n\033[1;36mO menor número gerado pela máquina foi {}'
      .format(maior, menor))
