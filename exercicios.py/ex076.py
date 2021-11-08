# fazer uma tupla com nome e valor de produtos e depois mostrar na tela de forma tabular e alinhada

produtos = 'Mouse', 230, 'Mousepad', 140, 'Teclado mecânico', 400, 'Placa de vídeo', 2000, 'Monitor', 700
for item in range(0, len(produtos)):
    if item % 2 == 0:
        print('\033[1m{:.<35}'.format(produtos[item]), end='')
    else:
        print('\033[1;32m R$\033[m\033[1m {:.2f}'.format(item))
# a principal lógica por tras do funcionamento da tabela é: criar um loop que vai iterar a cada index da tupla de
#  produtos, e quando o valor do index for par, significa que é uma string com nome do produto, pois ela começa no index
#   0 e vem após o preço sempre, ou seja, de 2 em 2 e a cada número par. já os preços se encontram no index impar sempre
#    caso o valor da iteraçao sobre o index seja ímpar, irá printar o numero.
