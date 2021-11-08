# funçao idade de voto que mostra se o voto vai ser obrigatorio, opcional ou negado
import datetime


def voto(nasc):
    idade = datetime.datetime.now().year - nasc
    if idade <= 16:
        print(f'\nCom {idade} anos, voto opcional.')
    elif 18 > idade > 16:
        print(f'\nCom {idade} anos, voto opcional.')
    elif 18 < idade < 65:
        print(f'\nCom {idade} anos, voto obrigatório!')
    elif idade > 65:
        print(f'\nCom {idade} anos, voto opcional')


ano = int(input('Insira o ano de nascimento: '))
voto(ano)

# a funçao tem como parametro a data de nascimento e calcula a idade do usuário, de acordo com a idade printa
#  a sua situaçao a respeito do voto.
