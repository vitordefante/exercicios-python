# lista que le nome do aluno e duas notas,guarda tudo numa listra e mostra a media,e as notas de cada aluno invidividual
alunos = []
aluno = []

while True:

    aluno.append(str(input('Nome: ').strip()))
    aluno.append(float(input('Nota 1: ')))
    aluno.append(float(input('Nota 2: ')))
    alunos.append(aluno[:])
    aluno.clear()

    continuar = str(input('Quer continuar? [S/N] ')).upper().strip()
    if continuar != 'S' and continuar != 'N':
        continuar = str(input('Caractere inválido, utilize apenas S/N: '))
    elif continuar == 'N':
        break


print('\n\033[1mNo.  Nome    {:>25}'.format('Média\033[m'))
for b in range(0, len(alunos)):
    print('{}    {:<25}{}'.format(b, alunos[b][0], (alunos[b][1] + alunos[b][2]) / 2))


notas = 0
while True:

    notas = int(input('\n\033[1mMostrar as notas de qual aluno? (-1 interrompe): \033[m'))

    while notas > len(alunos):
        notas = int(input('\033[1mAluno inválido! Tente apenas com os alunos no boletim: '))
        if notas <= len(alunos):
            print('')

    if notas == -1:
        print('\033[1;33mEncerrando o programa...\033[m')
        break

    print('\033[1mNotas de {} sao {}'.format(alunos[notas][0], alunos[notas][1:]))
