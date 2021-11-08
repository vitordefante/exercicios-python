pessoas = []
pessoa = []
pesos = []
total = 0

# loop para colocar os dados dentro das listas
while True:
    pessoa.append(str(input('\033[1mNome: ')))
    pessoa.append(float(input('Peso: ')))
    total += 1  # contador de loopings feitos ( total de pessoas inseridas )
    pessoas.append(pessoa[:])  # pega uma copia da lista da pessoa individual, e joga dentro da lista de pessoas
    pesos.append(pessoa[1])  # pega o peso que se encontra no index 1 da lista de pessoa e joga em pessoas
    pessoa.clear()  # limpa a lista da pessoa individual para o proximo loop, assim mantendo so uma pessoa a cada loop

    continuar = str(input('Deseja continuar? [S/N]: ')).strip().upper()  # validaçao padrao para continuar ou nao
    if continuar != 'S' and continuar != 'N':
        continuar = str(input('Responda apenas usando [S/N]: '))
    elif continuar == 'N':
        break


print('\nAo todo, você cadastrou {} pessoas.'.format(total))  # printa o total de pessoas

# nome pessoas maior peso
print('O \033[1;31mmaior\033[m\033[1m peso foi de {}kg. Peso de '.format(max(pesos)), end='')
for p in pessoas:
    if p[1] == max(pesos):  # se o peso da pessoa for igual ao maior peso
        print('{}.. '.format(p[0]), end='')  # será printado o nome dela. index[0] da iteraçao p sobre a lista

# nome pessoas menor peso
print('\nO \033[1;32mmenor\033[m\033[1m peso foi de {}kg. Peso de '.format(min(pesos)), end='')
for L in pessoas:
    if L[1] == min(pesos):
        print('{}.. '.format(L[0]), end='')
print('\n')

# o nome e o peso de cada pessoa é uma sublista dentro de uma lista, e para encontrar os dados requisitados no exercicio
#  foi necessário iterar sobre a lista no index especificado para cada dado, sendo nome pessoas[0] e o peso pessoas[1]
