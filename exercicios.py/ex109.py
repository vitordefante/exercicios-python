from exercicios.modulos import moeda

x = float(input('Digite o preço: '))
print(f'A metade de {moeda.moeda(x)} é {moeda.metade(x, True)}')
print(f'O dobro de {moeda.moeda(x)} é {moeda.dobro(x, True)}')
print(f'Aumentando 10% de {moeda.moeda(x)} temos {moeda.aumentar(x, 10, True)}')
print(f'Reduzindo 13% de {moeda.moeda(x)} temos {moeda.diminuir(x, 13, True)}')

# Atualizaçao de todas as funçoes. Agora todas as funçoes possuem um parametro opcinal reais=False
#  que permite retornar o valor formatado na moeda reais ou nao, feito com a funçao moeda.
