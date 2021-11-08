# programa que leia um ano e diga se ele é bissexto
ano = (int(input('Insira um ano para saber se ele é bissexto ou nao: ')))
bissexto = ano % 4
if bissexto == 0 and bissexto % 100 != 0 or bissexto % 400 == 0:
    print('\n{} é um ano bissexto.'.format(ano))
else:
    print('\n{} nao é um ano bissexto.'.format(ano))

# também é possível colocar o operador de resto na mesma linha na funçao if, exemplo = if ano % == 0 ...
