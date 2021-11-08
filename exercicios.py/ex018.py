from math import sin, cos, tan, radians
angulo = float(input('Insira o angulo para ter o valor do seno, cosseno e tangente: '))
seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))
print('sin {:.2f}, cos {:.2f}, tan {:.2f}'.format(seno, cosseno, tangente))
