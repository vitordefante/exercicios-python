from exercicios.modulos import moeda

x = float(input('Digite o preço: '))
print(f'A metade de {x} é {moeda.metade(x)}')
print(f'O dobro de {x} é {moeda.dobro(x)}')
print(f'Aumentando 10% de {x} temos {moeda.aumentar(x, 10)}')
print(f'Reduzindo 13% de {x} temos {moeda.diminuir(x, 13)}')

# foram feitas algumas funçoes no módulo moeda que se encontra dentro do pacote modulos, o programa
#  importou esses módulos e utilizou eles nos prints
