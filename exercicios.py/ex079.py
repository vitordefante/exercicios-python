#  inserir numeros em uma lista, caso ja tenha, nao inserir, no final mostrar os números
numeros = []
while True:
    numero = int(input('Insira um número inteiro: '))
    numeros.append(numero)
    if numeros.count(numero) >= 2:
        print('\033[1;33mEsse número já foi inserido portanto nao contará.\033[m')
        del numeros[-1]
    else:
        print('Número adicionado com sucesso...')
    continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()
    if continuar == 'N':
        break
print(f'\nOs números digitados em ordem crescente sao: {sorted(numeros)}')
