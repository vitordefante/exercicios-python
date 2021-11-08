# minijogo de adivinhar numero aleatorio gerado pela maquina
from random import randint
print('Gerando um número de 1 a 5...')
numero = (randint(1, 5))
adivinhe = int(input('Insira o número que você acha que foi gerado pela maquina: '))
if numero == adivinhe:
    print('Parabéns! Você acertou o número escolhido pela máquina que é {}.'.format(numero))
else:
    print('Você errou! O número gerido pela máquina foi {}, e nao {}.'.format(numero, adivinhe))
# filtrar caracteres e letras do input a fim de evitar erros no programa por descuido do usuário
