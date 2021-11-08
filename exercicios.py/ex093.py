# mostra aproveitamento de um jogador

gols = []
total = 0

jogador = {'nome': str(input('Nome: ')).strip(),
           'gols': [],
           'total': total}
quant = int(input('Quantas partidas {} jogou? '.format(jogador['nome'])))

for x in range(1, quant + 1):
    gol = (int(input('Quantos gols na partida {}? '.format(x))))
    jogador['total'] += gol
    gols.append(gol)
    jogador['gols'].append(gol)
    gols.clear()

print('')
print(jogador, '\n')

for x, y in jogador.items():
    print('O campo {} tem valor {}'.format(x, y))
cont = 1
print('\nO jogador {} jogou {} partidas.'.format(jogador['nome'], quant))
for x in jogador['gols']:
    print('Na partida {}, fez {} gols.'.format(cont, x))
    cont += 1
print('Foi um total de {} gols.'.format(jogador['total']))

# o funcionamento do programa baseia-se inserçao de listas dentro de dicionários, indexaçao e iteraçao composta
#   dentro de dicionarios, usando funçoes como ''for x, y in dicionario.items()'' .sendo  x = chave, y = valor