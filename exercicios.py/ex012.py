n1 = float(input('Insira o valor do produto desejado para receber o valor atualizado com 5% de desconto: '))
n2 = 5*n1
n3 = n2/100
n4 = n1-n3
print('\nO valor do produto com desconto aplicado fica {:.2f} R$.'.format(n4))
