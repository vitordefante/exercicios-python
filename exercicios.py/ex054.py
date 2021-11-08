#  programa que le o ano de nascimento de sete pessoas e mostra quantas atingiram a maioridade e quantas nao
import datetime
count = 0
ano = datetime.datetime.now().year
for idade in range(1, 8):
    nascimento = int(input('Insira aqui seu ano de nasicmento: '))
    idade1 = ano - nascimento
    if idade1 >= 21:
        count = count + 1
print('\033[1;32m{}\033[m pessoas das 7 inseridas já atingiram a \033[1;32mmaioridade\033[m.'.format(count))
