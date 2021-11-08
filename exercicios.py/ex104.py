def leiaInt(txt):
    """"Funçao que analisa se o input do usuário é um número ou nao.
        param txt: O texto texto que sera printado para o input de n, ex: 'Insira um número: '
        return: retorna o valor inserido, se o mesmo for numérico, caso nao seja, é mostrado
        uma mensagem de erro e solicitado novamente o input, até que seja um número."""
    n = input(f'{txt}')
    while not n.isnumeric():
        print('\033[1;31mERRO! Digite um número inteiro válido.\033[m')
        n = input(f'{txt}')
    return n


a = leiaInt('Insira numero: ')
print(f'Você acabou de digitar o número {a}')
help(leiaInt)
