# programa que mostra a tabuada do numero que o usuario inserir. o prorama para quando o numero for negativo
cont = 0
tab = int(input('\033[1;34mInsira o número do qual deseja ver a tabuada:\033[m '))
while tab >= 0:  # enquanto a tabuada nao atinge o flag, que é um número negativo
    cont += 1  # contagem para a tabuada do 1 até o 10
    print('{} x {} = {}'.format(tab, cont, tab * cont))
    if cont == 10:  # quando a contagem atingir o décimo número, ou numero x 10
        cont = 0  # zerando a contagem e encerrando a tabuada do número inserido
        tab = int(input('\n\033[1;34mInsira o número do qual deseja ver a tabuada: \033[m'))  # novo input para nova tab
print('\033[1mEncerrando a tabuada, volte sempre...')
