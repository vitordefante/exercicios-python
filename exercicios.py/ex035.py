# programa que lê três retas e informa se elas formam ou nao um triângulo
a = float(input('Insira o comprimento da primeira reta: '))
b = float(input('Insira o comprimento da segunda reta: '))
c = float(input('Insira o comprimento da terciera reta: '))
if a < b + c and b < a + c and c < a + b:
    print('Os segmentos acima formam um triângulo')
else:
    print('Os segmentos acima nao formam um triângulo')
