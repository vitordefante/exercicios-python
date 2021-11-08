# crie um programa que mostre se o nome da cidade inserida começa com SANTO
cidade = input('Insira o nome da cidade: ').upper()
santo = cidade.split()
if 'SANTO' in santo[0]:
    print('A cidade inserida POSSUI Santo no nome.')
else:
    print('A cidade inserida NAO POSSUI Santo no nome.')
