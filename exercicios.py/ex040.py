# calcular duas notas de um aluno e mostrar a média, com uma mensagem no final
nota1 = float(input('Insira aqui a sua primeira nota: '))
nota2 = float(input('Insira aqui sua segunda nota: '))
media = (nota1 + nota2) / 2
if media < 5:
    print('\n\033[1;31m     REPROVADO\n     Média: {}'.format(media))
elif media >= 5 and media < 6.9:   # simplificar essa linha
    print('\n\033[1;33m     RECUPERAÇAO\n     Média {}'.format(media))
else:
    print('\n\033[1;34m     APROVADO\n     Média {}'.format(media))
