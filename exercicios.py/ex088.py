#  mega sena
from random import randint
from time import sleep

quant = int(input('Quantos jogos deseja que seja sorteado? '))

print('\n\033[1;35mGerando os palpites...\033[m\033[1m')
sleep(1)

for x in range(0, quant):
    numeros = [randint(0, 60), randint(0, 60), randint(0, 60), randint(0, 60), randint(0, 60), randint(0, 60)]
    for r in numeros:
        if numeros.count(r) >= 2:
            end = numeros.index(r)
            numeros[end] = randint(0, 60)
    sleep(0.5)
    print('Jogo {}: {}'.format(x + 1, numeros))