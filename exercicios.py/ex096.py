# programa que tenha uma funçao area() que recebe as dimensoes de um terreno retangular e mostre a area
def area(a, b):
    print('\nA área de um terreno {} x {} é de {:.1f}m²'.format(a, b, a * b))


print('\033[1mControle de terrenos\n')
L = float(input('Largura (m): '))
C = float(input('Comprimento (m): '))
area(L, C)

# a funçao criada apenas mostra na tela a area e a comprimento, e o produto de ambos (a * b) = m²

