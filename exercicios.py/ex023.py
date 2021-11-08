# programa que leia um número de 0 a 9999 e mostre os digitos separadamente
num = int(input('A seguir insira um número de 0 a 9999 para receber seus digitos separadamente: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Analisando o número {}...'.format(num))
print('O milhar é {}'.format(m))
print('A centena é {}'.format(c))
print('A dezena é {}'.format(d))
print('A unidade é {}'.format(u))
