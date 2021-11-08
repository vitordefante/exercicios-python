# faça um programa que leia 3 numeros e mostre qual é o maior e qual é o menor
print('Insira três números inteiros para saber qual o maior e qual o menor\n')
a = int(input('Insira aqui o primeiro numero: '))
b = int(input('Insira aqui o segundo número: '))
c = int(input('Insira aqui o terceiro número: '))
# Verificando o menor algarismo
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
# Verificando o maior algarismo
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print('\nO maior número inserido foi {}.'.format(maior))
print('O menor número inserido foi {}.'.format(menor))
# O os valores atribuidos nos '' if's '' pode ser também inserido nos colchetes {}
# Os valores podem ser alterados dentro do if, exemplo menor = a if b < a menor = b
