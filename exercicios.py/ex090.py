# le um aluno e média e mostra sua situaçao

aluno = {'nome': str(input('Nome: ')).strip().title()}
aluno['media'] = float(input('Média de {}: '.format(aluno['nome'])))
print('\nO nome é igual a {}, e sua média é {}'.format(aluno['nome'], aluno['media']))
if aluno['media'] >= 7:
    print('{} está aprovado.'.format(aluno['nome']))
elif aluno['media'] >= 5:
    print('{} está de recuparaçao'.format(aluno['nome']))
else:
    print('{} está reprovado(a).'.format(aluno['nome']))
