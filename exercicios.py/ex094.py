pessoas = []
media = 0
cont = 0
while True:
    pessoas.append({'nome': str(input('Nome: ')).strip(),
                    'sexo': str(input('Sexo: [M/F]: ').strip().upper()),
                    'idade': int(input('Idade: '))})

    continuar = str(input('Quer continuar? [S/N]: ')).strip().upper()
    if continuar != 'S' and continuar != 'N':
        continuar = str(input('Use apenas [S/N]: ')).strip().upper()
    elif continuar == 'N':
        break

print('\nO grupo tem {} pessoas.'.format(len(pessoas)))

for x in range(0, (len(pessoas))):
    media += pessoas[cont]['idade']
    cont += 1

print('A média de idade é {:.1f}'.format(media / len(pessoas)))

cont = 0
print('As mulheres cadastradas foram: ', end='')
for m in range(0, len(pessoas)):
    if pessoas[m]['sexo'] == 'F':
        print('{}...'.format(pessoas[m]['nome']), end='')

cont = 0
print('\n\nLista de pessoas com idade acima da media: ')
for v in range(0, len(pessoas)):
    if pessoas[v]['idade'] > media / len(pessoas):
        for p, i in pessoas[v].items():
            print('{} = {}; '.format(p, i), end='')
            cont += 1
            if cont == 3:
                print('')
                cont = 0
