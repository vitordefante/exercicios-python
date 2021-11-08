times = 'Atletico mineiro', 'Palmeiras', 'Flamengo', 'Fortaleza', 'Bragantino', 'Corinthians,', 'Internacional', \
        'Fluminense', 'Cuiaba', 'Athletico-PR', 'Atletico Goianiense', 'Sao Paulo', 'Ceara', 'Santos', 'Bahia',\
        'America-MG', 'Juventude', 'Gremio', 'Sport Recife', 'Chapecoense'
chape = times.index('Chapecoense')
print('\nOs cinco primeiros times da tabela sao: {}'.format(times[0:5]))
print('\nOs quatro últimos times da tabela sao: {}'.format(times[-4:]))
print('\nA ordem alfabéticas dos times fica: {}'.format(sorted(times)))
print('\nO time da chapecoense se encontra na {}° posiçao na tabela'.format(chape + 1))
