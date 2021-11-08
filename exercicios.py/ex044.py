# Programa que calcula valor a ser pago por um prodto, considerando o preço inical e a condiçao de pagamento
# As condiçoes de pagamento serao: dinheiro/cheque: 10% off, cartao a vista: 5% off, ate 2x cartao: 0%off
# 3x ou mais  no cartao: 20% de juros
valor = float(input('Insira a seguir o valor do produto: '))
forma = int(input('\nEscolha sua forma de pagamento.\nPara pagar no \033[1;32mdinheiro\033[m digite \033[1;32m1\033[m'
                  ' \nPara pagar no \033[1;34mcheque\033[m'
                  ' digite \033[1;34m2\033[m \nPara pagar no \033[1;35mcartao\033[m digite \033[1;35m3\033[m\n'))
if forma == 1 or forma == 2:
    print('O valor final do produto é de \033[1;32mR${:.2f}\033[m com 10% de desconto aplicado.'
          .format(valor - (10/100 * valor)))
if forma == 3:
    parcelamento = int(input('Deseja pagar seu produto em quantas vezes no \033[1;35mcartao\033[m? '))
    if parcelamento == 1:
        print('O valor final do produto é de \033[1;32mR${:.2f}\033[m com 5% de desconto aplicado.'
              .format(valor - (5/100 * valor)))
    elif parcelamento == 2:
        print('O valor total do seu produto é \033[1;32mR${:.2f}\033[m, parcelado em {}x de \033[1;32mR${:.2f}\033[m.'
              .format(valor, parcelamento, valor / 2))
    elif parcelamento >= 3:
        print('O valor total do seu produto é de \033[1;32mR${:.2f}\033[m, parcelado em {}x de \033[1;32mR${:.2f}\033[m.'
              .format(valor + (20/100 * valor), parcelamento, (valor + (20/100 * valor)) / parcelamento))
        print('Há um \033[1;31mjuros\033[m de \033[1;31m20%\033[m sob o valor inicial do produto devido ao parcelamento a partir de 3x!')
