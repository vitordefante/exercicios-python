def leiaInt(txt):


    try:
        inteiro = int(input(f'{txt}'))

    except ValueError:

        print('\033[1;31mErro! Por favor, digite um número inteiro válido.\033[m')
        inteiro = int(input('Insira um número inteiro: '))

    return inteiro


a = leiaInt('Insira numero: ')
print(f'Você acabou de digitar o número {a}')
