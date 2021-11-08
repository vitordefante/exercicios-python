from exercicios.modulos import moeda

x = float(input('Digite o preço: '))
print(f'A metade de {moeda.moeda(x)} é {moeda.metade(x, True)}')
print(f'O dobro de {moeda.moeda(x)} é {moeda.moeda(moeda.dobro(x))}')
print(f'Aumentando 10% de {moeda.moeda(x)} temos {moeda.moeda(moeda.aumentar(x, 10))}')
print(f'Reduzindo 13% de {moeda.moeda(x)} temos {moeda.moeda(moeda.diminuir(x, 13))}')

# exercicio 107 atualizada com uma nova funçao moeda() que transoforma o parametro inserido em reais (R$)
