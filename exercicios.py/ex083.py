exp = str(input('\033[1mInsira aqui sua expressao: '))
par = []
for simb in exp:
    if simb == '(':
        par.append('(')
    elif simb == ')':
        if len(par) > 0:
            par.pop()
        else:
            par.append(')')
            break
if len(par) == 0:
    print('\nA expressao inserida é \033[1;32mválida\033[m\033[1m!')
else:
    print('\nA expressao inserida é \033[1;31minválida\033[m!')

#  a lógica de funcionamento desse aplicativo é: toda vez que o laço itera a expressao é ela é um '(', esse parenteses
#   é adicionado na lista par. E toda vez que o laço itera sobre um parenteses fechando ')' ele remove o parenteses
#    que está abrindo. Entao, se a lista de paresnteses nao estiver vazia, a expressao nao está válida.
#     Caso a lista esteja vazia o programa mostra que a expressao é válida pois todos os parenteses abrindo tiveram
#      seus devidos desfechos.
