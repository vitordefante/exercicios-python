# simulador de caixa eletrônico

green = '\033[1;32m'
none = '\033[m\033[1m'

cinq = 0
vint = 0
dez = 0
um = 0

valor = int(input('\033[1m\nInsira o valor que deseja sacar: '))
sacado = 0
while sacado < valor:
    cinq = int(valor / 50)
    valor = valor - (cinq*50)
    vint = int(valor / 20)
    valor = valor - (vint * 20)
    dez = int(valor / 10)
    valor = valor - (dez * 10)
    um = int(valor / 1)
    valor = valor - (um * 1)
print('\nSaque efetuado! Foram utilizadas:\n{} notas de R$50\n{} notas de R$20\n{} notas de R$10\n{} notas de R$1'
      .format(cinq, vint, dez, um))

''' "eu:" o script funciona de maneira que se o valor for dividido por o valor de uma nota que nao é necessária, o valor
   retornado da divisao será 0 portanto nao será somado no valor, exemplo:
            valor de saque = 235
            cinq  = int(valor / 50)  # < total de notas de 50 necessárias para o valor do saque
            valor = valor - (cinq (4) *50)
            valor = 235  - ( 4 * 50 ) =  234 - 200
            valor = valor - 200 / valor = 35
            vint  = int(valor(30) / 20)  # < quantidade de notas de 20)
            vint = 1 (float 1.5 convertido para int 1 ) # < vint recebe 1 nota no saque
            valor = valor - (1 * 20) 
            valor = 15.... assim vai, até tirar uma nota de R$10 e cinco notas de R$1.
            
    Guanabara:A soloçao do professor guanabara se baseia na alteraçao das cédulas caso o total
                   nao seja maior que a cédula. Se o total for maior que a cédula, é possível subtrair
                o valor da cédula sob o total, se nao, nao.
                 Quando o total se torna menor do que cédula, o valor da cédula é alterado até chegar 
                 na cédula de R$1, e até o valor total ser sacado. script a seguir:
                 while Trule:
                 if total >= ced: < se o total for maior que o valor da cédula
                    total -= <é subtraído o valor cédula sob o total a ser sacado
                    totalced += 1 < a cédula em questao recebe +1 na sua contagem de vezes
                else:
                    if ced == 50:  < transformando em cédulas menores caso a condiçao seja False
                        ced = 20
                    if etc....'''
