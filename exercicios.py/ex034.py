# programa que le salario e calcula aumento. se aumento >= 1250 = 10%+ if <=1250 = +15%
renda = float(input('Insira aqui o valor do seu salário para calcular o aumento: '))
aumento1 = (renda*10)/100 + renda
aumento2 = (renda*15)/100 + renda
if renda > 1250.0:
    print('O seu salário após o aumento será de R${:.2f}'.format(aumento1))
if renda <= 1250.0:
    print('O seu salário após o aumento será de R${:.2f}'.format(aumento2))
