# programa que mostra na tela uma contagem regressiva para o estouro de fogos de artificio
# contagem de 0 a 10, com 1 segundo de pausa entre eles
import time
print('\033[1;35mINICIA-SE AGORA A CONTAGEM REGRESSIVA PARA O ESTOURO DOS FOGOS!\033[1;36m')
for c in range(10,0,-1):
    print(c)
    time.sleep(1)
print('\033[1;34mA queima dos fogos se inicia agora! Feliz ano novo!')
