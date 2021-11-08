# relogio 12 horas
from time import sleep

hora = 0
horas = 0
minutos = 0

while True:
    minutos += 1
    if minutos > 59:
        horas += 1
        minutos = 0
        if horas == 12:
            horas = 0
    if horas < 10:
        print(f'0{horas}:', end='')
    elif horas >= 10:
        print(f'{horas}:', end='')
    if minutos < 10:
        print(f'0{minutos}')
    if minutos >= 10:
        print(f'{minutos}')
    sleep(0.3)
    # sleep(0.18)

# o programa imprime um 0 na frente das horas e dos minutos caso eles sejam menor que 10
