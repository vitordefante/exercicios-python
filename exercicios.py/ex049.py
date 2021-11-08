# programa que lê um número e mostra sua tabuada do um até o 10
numero = int(input('Insira  o número que deseja a tabuada: '))
for x in range(1, 11):
    print('{} x {} = {}'.format(numero, x, numero * x))
# a funçao for executa um comando por quantas vezes for determinado, na ordem em que foi determinado
