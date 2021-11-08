import datetime

pessoa = {}
ano = datetime.date.today().year
pessoa['Nome'] = str(input('Nome: '))
pessoa['Idade'] = ano - int(input('Ano de nascimento: '))
pessoa['CTPS'] = int(input('Carteira de trabalho: [0 sem]: '))
if pessoa['CTPS'] != 0:
    pessoa['Contrataçao'] = int(input('Ano de contrataçao: '))
    pessoa['Salário'] = float(input('Salário: R$'))
    pessoa['Aposentadoria'] = pessoa['Idade'] + ((pessoa['Contrataçao'] + 35) - datetime.date.today().year)
print('')

for x, y in pessoa.items():
    print('{} tem o valor de {}'.format(x, y))

# logica de funcionamento do aplictavivo resume-se a indexaçao comum de dicionários e uso de estrutura condicional
