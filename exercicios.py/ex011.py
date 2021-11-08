print('Faça um programa que leia a altura e a largura de uma parede, calcule sua area e a quantidade de tinta necessár'
      'ia, sabendo que cada litro de tinta pinta 2m²')
print(' ')
print('A seguir, insira a altura e a largura da parede em metros para saber sua área e a quantidade necessária de tinta'
      ' para pinta-la')
print(' ')
altura = float(input('Altura da parede: '))
largura = float(input('Largura da parede: '))
area = altura*largura
tinta = area/2
print('Sua parede ocupa {:.2f}m² e será preciso {:.2f} litros de tinta para pinta-la.'.format(area, tinta))
