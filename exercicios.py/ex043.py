# faça um programa que tire a medida do IMC e mostre suas informaçoes a respeito
peso = float(input('Insira seu peso em quilogramas (kg): '))
altura = float(input('Insira sua altura em metros (m): '))
imc = peso / (altura ** 2)  # altura elevado a 2 (altura²)
if imc < 18.5:
    print('\n\033[1;34mVocê está levemente abaixo do peso.')
elif imc > 18.5 and imc < 25:
    print('\n\033[1;32mVocê está no peso ideal.')
elif imc > 25 and imc < 30:
    print('\n\033[1;33mVocê está acima do peso ideal')
elif imc > 30 and imc < 40:
    print('\n\033[1;31mVocê está em nível de obesidade')
else:
    print('\n\033[1;31;40mVocê está em nível de obesidade morbida\033[m')
print('\033[1;mO valor do seu imc é de {:.2f}kg/m².'.format(imc))
