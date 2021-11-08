# ler idade e sexo de varias pessoas e mostrar quantas tem +18, homens cadastrados, e mulheres -20
maior = 0
homens = 0
mulher20 = 0
while True:
    sexo = str(input('\033[1mDigite seu sexo usando \033[1;36mH\033[m ou \033[1;35mM: \033[m')).upper().strip()
    if 'H' not in sexo and 'M' not in sexo:
        print('\033[1mOpçao inválida, tente novamente utilizando apenas H ou M.')
        continue
    idade = int(input('\033[1mDigite sua idade: \033[m'))
    if idade >= 18:
        maior += 1
    if 'H' in sexo:
        homens += 1
    if 'M' in sexo and idade < 20:
        mulher20 += 1
    continuar = str(input('\033[1mDeseja continuar? [S/N]: ')).upper().strip()
    if 'N' in continuar:
        break
    elif 'N' and 'S' not in continuar:
        print('Input \033[1;31minválido\033[m, continuando o programa...')
print('\n\033[mForam cadastradas \033[1;32m{}\033[m pessoas maiores de idade, \033[1;34m{} homens\033[m e \033[1;35m{} mulheres com menos de 20 anos.'.
      format(maior, homens, mulher20))
