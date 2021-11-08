print(' ')
n1 = float(input('Insira o valor em reais para converter em dólar e em renminbi: '))
n2 = n1*0.19012
n3 = n1*1.23039
print(' ')
print('O valor inserido vale ${:.2f} dólares e ¥{:.2f} yuan '.format(n2, n3))
