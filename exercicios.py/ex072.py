# tupla que le um numero inteiro e entrega o texto do numero inteiro
numeros = ('zero um dois tres quatro cinco seis sete oito nove dez onze doze treze quatorze quinze dezesseis dezessete '
           'dezoito dezenove vinte').split()
while True:
    extenso = int(input('\033[1mDigte o número entre 0 e 20 que deseja ver por extenso(-1 para sair): '))
    if extenso == -1:
        print('Encerando o programa...')
        break
    while extenso < 0 or extenso > 20:
        extenso = int(input('\033[1mNúmero inválido, insira um número entre 0 e 20: '))
    print('Você digitou o número \033[1;33m{}\033[m\n'.format(numeros[extenso]))
#  a lógica principal de funcionamento do aplicativo gira em torno do print numeros[numimput] onde irá
#         printar o endereço da tupla que vai ser o input do usuário (se for entre 0 e 20)
