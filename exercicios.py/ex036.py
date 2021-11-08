# programa para aprovar empréstimo bancário na compra de uma casa nas dadas condiçoes
# o programa deve perguntar o valor da casa, salário do comprador e em quantos ano ele vai pagar
# após dadas condiçoes, calcular a prestaçao mensal, sabendo que ela NAO pode exceder 30% do salário.
print('Abaixo, insira as informaçoes requisitadas para analisarmos a possibilidade do seu empréstimo')
valor = float(input('Insira o valor da casa: R$ '))
salario = float(input('Digite a seguir o valor da sua renda salarial mensal: R$ '))
anos = int(input('Em quantos anos você pretende pagar a casa? '))
meses = anos * 12
prestacao = valor / meses
if prestacao > (30 / 100) * salario:
    print('\nInfelizmente sua solicitaçao para o empréstimo nao foi aprovada.')
else:
    print('\nSua solicitaçao de empréstimo foi aprovada, as parcelas terao um valor de {:.2f} ao mês durante {} anos.'
          .format(prestacao, anos))
