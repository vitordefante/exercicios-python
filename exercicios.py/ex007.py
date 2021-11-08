# Faça um programa que calcule duas notas e mostre sua média')
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
n3 = (n1+n2)/2
if n3 >= 6:
    print('Parabéns,sua nota foi {} e está dentro da média, você foi aprovado'.format(n3))
else:
    print('Sua nota final foi {} e está abaixo da média, você foi reprovado.'.format(n3))
# fazer um programa que calcule a quantidade de notas que o úsuario inserir e dar uma média