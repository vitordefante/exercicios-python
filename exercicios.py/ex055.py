#  programa que lê o peso de 5 pessoas e no final mostra qual foi o maior e qual foi o menor peso lido.
pessoas = []  # lista vazia a ser preenchida pelo input
for pesos in range(1, 6):  # loop para o usuario fazer o input do peso de cada pessoa
    peso = float(input('Insira o peso da {}° pessoa (kg): '.format(pesos)))
    pessoas.append(peso)  # .append para inserir os inputs em uma lista
print('A pessoa mais \033[1;31mpesada\033[m pesa \033[1;31m{:.2f} kg\033[m e a mais \033[1;34mleve\033[m pesa \033[1;34m{:.2f} kg'
      .format(max(pessoas), min(pessoas)))
