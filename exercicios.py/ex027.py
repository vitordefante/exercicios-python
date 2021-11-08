# programa que le o nome completo de uma pessoa e mostra o primeiro e ultimo nome
nome = input('Digite seu nome completo: ')
nomecompleto = nome.split()
primeiro = nomecompleto[0]
ultimo = nomecompleto[-1]
print('Seu primeiro e último nome sao, respectivamente {} e {}'.format(primeiro.title(), ultimo.title()))
# pesquisar sobre como printar as strings splitadas sem [] e ''
