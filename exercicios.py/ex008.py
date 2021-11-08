print('Faça um programa que leia uma medida em metros e transofrme em centimetros e milímetros.')
print(' ')
print('Coloque o valor em metros abaixo para a fazer a converçao pra centímetros e milímetros')
print(' ')
n1 = float(input('Insira o valor em metros: '))
dm = n1*10
cm = n1*100
mm = n1*1000
dam = n1/10
hm = n1/100
km = n1/1000
print('Milímetros: {}mm'.format(mm))
print('Centímetros: {}cm'.format(cm))
print('Decâmetros: {}dam'.format(dam))
print('Hectómetros: {}hm'.format(hm))
print('Quilômetros: {}km'.format(km))
