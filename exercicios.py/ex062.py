# melhore o desafio 61, lendo o primeiro termo e a razao de uma PA, mostrando os 10 primeiros termos da progressao
# usando a estrutura while, e mostrando quantos o usuario desejar a mais
t1 = float(input('Insira o primeiro termo da razao: '))
r = float(input('Insira a razao da p.a: '))
enesimo = 1  # valor do enesimo numero da progressao para o segundo loop
cont = 0  #contador do primeiro loop para determinar quantas vezes ele será executado para mostar os 10 primeiros termos
cont1 = 0  # contador para o segundo loop para mostar quantos termos o usuário desejar
prog = 0  # valor da progressao para usar no segundo loop como base para exibir os termo em diante
print('\n\033[1;35mOs 10 primeiros números da progressao aritimética sao:\033[1;32m')
print(t1)  # primeiro termo
while cont <= 8:  # loop de 0 até 8 para mostrar o 9 termos sequentes do primeiro nos primeiros 10 termos da progressao
    if cont <= 8:  # condiçao para executar o loop
        cont = cont + 1  # contagem de 1 em 1 a cada loop até chegar em 8 para encerra-lo
        prog = (t1 + r * cont)  # valor da progressao para ser exibido a cada loop, a cada loop cont recebe + 1
        print(prog)
enesimo = int(
    input('\033[1;35mDeseja ver mais quantos termos dessa progressao? \033[1;32m'))  # entrada de termos para o 2° loop
if enesimo != 0:  # condiçao para executaro loop = se o usuario deseja mais que 0 progressoes
    while cont1 < enesimo:  # loop será executado até a contagem chegar na quantidade de termos extras da p.a
        cont1 = cont1 + 1  # acrescentando valor na contagem a cada loop
        prog1 = prog + (r * cont1)  # prog1 é o novo valor da progressao, o valor de quantos termos extras da p.a
        print(prog1)
        if cont1 >= enesimo:  # quando a contagem se igualar a quantidade de termos extras desejados pelo user
            prog = prog1  # IMPORTANTE, a primeira prog se iguala a prog1, para a p.a continuar da onde parou no loop antecedente
            cont1 = 0  # zerando a contagem para o próximo loop de de termos extras
            enesimo = int(input('\033[1;35mDeseja ver mais quantos termos dessa progressao? \033[1;32m'))  # novo input de quantos termos serao mostrados
            if enesimo == 0:  # desliga o programa
                print('\n\033[1;33mEncerrando o programa...')
                break
