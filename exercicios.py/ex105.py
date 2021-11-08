# funçao que pega as notas dos alunos e as transforma em dicionário
def notas(*n, sit=False):
    """"Funçao para analisar notas e situaçoes de vários alunos.
        param n: Uma ou mais notas dos alunos (aceita várias)
        param sit: Valor opcional, indicando se deve ou nao adicionar a situaçao
        return: dicionário com várias informaçoes sobre a situaçao da turma."""
    tudo = n
    soma = sum(tudo)
    tudo1 = {'total': len(n),
             'maior': max(tudo),
             'menor': min(tudo),
             'media': soma / len(n)}
    if sit:
        if soma / len(n) >= 8:
            tudo1['situaçao'] = 'Excelente'
        elif 8 > soma / len(n) >= 6:
            tudo1['situaçao'] = 'Razoável'
        elif 6 > soma / len(n) >= 5:
            tudo1['situaçao'] = 'Ruim'
        elif soma / len(n) < 5:
            tudo1['situaçao'] = 'Péssima'
    return tudo1


print(notas(4, sit=True))
