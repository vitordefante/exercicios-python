print(' ')
print('Insira a quantidade de quilometros rodados e dias desde o aluguel do veículo')
km = float(input('Quilometros rodados: '))
dias = float(input('Dias de utlizaçao: '))
valor = (dias*60) + (0.15*km)
print('O valor do aluguel é de {:.2f} R$'.format(valor))
