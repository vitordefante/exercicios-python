# programa que lê o primeiro termo e a razao de uma p.a e em seguida mostra os 10 primeiros termos dela
t1 = float(input('Insira o primeiro termo da P.A: '))
r = float(input('Insira a razao da P.A: '))
sum = 0  # <contador
print('\n\033[1;35mOs 10 primeiros números da progressao aritimética sao:\033[1;32m')
print(t1)  # primeiro termo da razao a ser mostrado na tela, é o valor inserido no t1
for i in range(1, 10):
    inicio = t1
    print(t1 + r * i)  # a funçao print vai exibir o segundo termo da da progresssao em diante
    #  t1 ( primeiro termo) + r ( razao da progressao ) vezes * i ( o laço que vai de 1 até 10 progressivamente)
