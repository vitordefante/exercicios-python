def ficha(nome='', gols=0):
    if nome == '':
        nome = '<desconhecido>'
    if gols == '':
        gols = 0
    if not gols.isnumeric():
        gols = 0
    print(f'O jogador {nome} fez {gols} gol(s) no campeonato.')


n = input('Nome do jogador: ')
g = input('Número de gols: ')
ficha(n, g)

# a funçao funciona recebendo (ou nao) um nome e uma quantidade de gols, ambos str. o funçao funciona
#  caso os parametros nao sejam satisfeitos, pois há um leve tratamento de erros.
