from math import sqrt
oposto = float(input('Insira o valor do cateto oposto: '))
adjacente = float(input('Insira o valor do cateto adjecente: '))
hipotenusa = (oposto**2) + (adjacente**2)
hipotenusa1 = sqrt(hipotenusa)
print('O comprimento da hipotenusa é {:.2f}'.format(hipotenusa1))
