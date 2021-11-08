# programa que le palavras em uma tupla e mostra as vogais dela
palavras = ('Carro', 'Motocicleta', 'Casa', 'Mouse', 'Teclado', 'Controle', 'Futebol')
for palavra in palavras:
    print('\n\033[1mNa palavra {} temos as vogais '.format(palavra), end='')
    for vogal in palavra:
        if vogal.lower() in 'AaEeIiOoUu':
            print('\033[1;34m', vogal, '\033[m', end='')
