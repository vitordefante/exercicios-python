jogadores = []

while True:
    jogador = {'nome': str(input('Nome: ')).strip().title(),
               'gols': []}

    quant = int(input('Quantas partidas {} jogou? '.format(jogador['nome'])))
    for x in range(1, quant + 1):
        gol = int(input('Quantos gols na partida {}? '.format(x)))
        jogador['gols'].append(gol)

    jogadores.append(jogador.copy())

    for v in jogador.values():
        del v

    continuar = str(input('Quer continuar? [S/N] ')).strip().upper()
    if continuar != 'S' and continuar != 'N':
        continuar = str(input('Digito inválido, utilize apenas S/N: '))
    if continuar == 'N':
        break

cont = ''
print('\n\033[1mNo.   Nome                       Gols                      Total \033[m')
for x in range(0, len(jogadores)):
    print('{:<6}{:<26}{:<29}{}'
          .format(x, jogadores[x]['nome'], str(jogadores[x]['gols']), sum(jogadores[x]['gols'])))
cont = 0
while True:
    dados = int(input('\nMostrar dados de qual jogador? '))

    if dados == 999:
        print('\033[1;33mEncerrando...\033[m')
        break
    while dados > len(jogadores) and dados != 999:
        dados = int(input('Nao há jogador com o código {}! Tente novamente: '.format(dados)))
        if dados == 999:
            print('\033[1;33mEncerrando...\033[m')
            break

    print('\nLevantamento do jogador {}:'.format(jogadores[dados]['nome']))

    for c in jogadores[dados]['gols']:
        print('No jogo {} fez {} gols'.format(cont + 1, c))
        cont += 1
    cont = 0
