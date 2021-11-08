# programa que lê a idade do usuario e mostra: se ainda precisa alistar, se é a hora, se ja passou
# o programa deve mostrar também quanto tempo falta ou quanto tempo ja passou do prazo
import datetime
nascimento = int(input('Insira aqui seu ano de nascimento: '))
ano = datetime.datetime.now().year
idade = ano - nascimento
restante = 18 - idade
passados = idade - 18
if ano - nascimento == 18:
    print('\n\033[1;33mVocê precisa se alistar esse ano.')
elif idade < 18:
    print('\n\033[1;34mVocê ainda tem {} ano(s) até a candidatura.'.format(restante))
else:
    print('\n\033[1;31mSua candidatura está {} ano(s) atrasada.\033[m \nSe você já se inscreveu, ignore esta mensagem.'
          .format(passados))
