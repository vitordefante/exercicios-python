# programa que lê o sexo de uma pessoa mas só aceita M ou F, caso esteja errado perça digitar novamente
genero = str(input('\033[1mInsira seu gênero utilizando apenas \033[1;34mM\033[m/\033[1;35mF\033[m: ').upper().strip())
while 'F' not in genero[0] and 'M' not in genero[0]:
    genero = str(input('\033[1;31mLetra inválida, tente novamente usando \033[1;34mM\033[m/\033[1;35mF\033[m: '))\
        .upper().strip()
if genero == 'M':
    print('\033[1;34mO genero inserido é masculino.')
elif genero == 'F':
    print('\033[1;35mO genero inserido é feminino.')
