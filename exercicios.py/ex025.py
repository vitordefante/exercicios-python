# programa feito para informar se o nome inserido possui SILVA
nome = input('Insira seu nome completo: ').upper()
silva = 'SILVA' in nome
print('O nome inserido possui Silva?', end=' ')
print(silva)
