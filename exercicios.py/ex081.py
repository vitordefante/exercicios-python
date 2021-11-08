# programa para ler varios numeros e colocar numa lista e diz quantos elementos, valores decrescentes, valor 5 na lista
lista = []
while True:
    lista.append(int(input('\033[1mDigite um número: ')))
    continuar = str(input('Deseja continuar? [S/N]: ')).strip().upper()
    while continuar != 'N' and continuar != 'S':
        continuar = str(input('Input inválido! Informe se deseja continuar apenas com S/N: ')).strip().upper()
    if continuar == 'N':
        break
print('\nForam inseridos {} numeros na lista.'.format(len(lista)))
print('Os valores em ordem descresente sao {}'.format(sorted(lista, reverse=True)))
print('O valor 5 foi digitado!') if lista.count(5) >= 1 else print('O valor 5 nao foi digitado.')
